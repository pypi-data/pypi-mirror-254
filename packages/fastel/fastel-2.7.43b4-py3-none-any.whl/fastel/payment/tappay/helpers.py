import json
from typing import Any, Dict, Optional
from uuid import uuid4

import boto3
from bson import json_util

from fastel.cart import Cart
from fastel.cart.datastructures import PaymentSubTypes
from fastel.collections import get_collection
from fastel.config import SdkConfig
from fastel.exceptions import APIException
from fastel.payment.common.models.callback import CallbackModel
from fastel.payment.tappay.gateway import TappayGateway
from fastel.payment.utils import PaymentStatus, auto_order_number
from fastel.utils import timestamp_postfix


class TappayHelper:
    def __init__(self, partner_key: str, merchant_id: str, stage: str) -> None:
        self.gateway = TappayGateway(
            partner_key=partner_key, merchant_id=merchant_id, stage=stage
        )

    def handle_callback(self, resp: Dict[str, Any]) -> None:
        status = resp.get("status", None)

        checkout_col = get_collection("checkout")
        profile_col = get_collection("private_profile")

        checkout = checkout_col.find_one({"order_number": resp["order_number"]})

        if not checkout:
            raise APIException(status_code=400, error="invalid_order", detail="")

        if status == 0:
            payment_status = PaymentStatus.SUCCESS
        else:
            payment_status = PaymentStatus.FAILURE

        if payment_status == PaymentStatus.SUCCESS:
            card_identifier = resp["card_identifier"]
            profile_col.update_one(
                {"owner": checkout["owner"]},
                {"$set": {f"credit_cards.{card_identifier}.enabled": True}},
            )

        stepfn = boto3.client("stepfunctions")
        callback_data = CallbackModel(
            order_id=checkout["order_number"],
            total=checkout["total"],
            payment_subtype=checkout["payment_subtype"],
            payment_status=payment_status,
            payment_transaction_detail=resp,
            payment_transaction_id=resp["rec_trade_id"],
        )
        stepfn.start_execution(
            stateMachineArn=SdkConfig.payment_stepfn_arn,
            name=timestamp_postfix(
                f"callback_{callback_data.order_id}_{callback_data.payment_status}"
            ),
            input=callback_data.json(),
        )

    def handle_3d_resp(self, resp: Dict[str, Any]) -> Dict[str, Any]:
        status = resp.get("status", None)

        if status == 0:
            if "card_secret" in resp:
                checkout_col = get_collection("checkout")
                checkout = checkout_col.find_one({"order_number": resp["order_number"]})

                card_secret = resp["card_secret"]
                card_info = resp["card_info"]
                card_identifier = resp["card_identifier"]

                profile_col = get_collection("private_profile")

                profile_col.update_one(
                    {"owner": checkout["owner"]},
                    {
                        "$set": {
                            f"credit_cards.{card_identifier}": {
                                "card_secret": card_secret,
                                "card_info": card_info,
                                "enabled": False,
                            }
                        }
                    },
                )
            return {"url": resp["payment_url"]}

        raise APIException(
            status_code=400, error="checkout_error", detail=resp.get("msg")
        )

    def handle_n3d_resp(
        self, checkout_dict: Dict[str, Any], resp: Dict[str, Any]
    ) -> Dict[str, Any]:
        status = resp.get("status", None)

        if status == 0:
            payment_status = PaymentStatus.SUCCESS
        else:
            raise APIException(
                status_code=400, error="payment_failed", detail=resp.get("msg", "")
            )

        callback_data = CallbackModel(
            order_id=checkout_dict["order_number"],
            total=checkout_dict["total"],
            payment_subtype=checkout_dict["payment_subtype"],
            payment_status=payment_status,
            payment_transaction_detail=resp,
            payment_transaction_id=resp.get("rec_trade_id"),
        )

        stepfn = boto3.client("stepfunctions")
        stepfn.start_execution(
            stateMachineArn=SdkConfig.payment_stepfn_arn,
            name=timestamp_postfix(
                f"callback_{callback_data.order_id}_{callback_data.payment_status}"
            ),
            input=callback_data.json(),
        )

        checkout_dict["payment_status"] = payment_status

        return json.loads(json_util.dumps(checkout_dict))  # type: ignore

    def refund(self, order: Dict[str, Any]) -> Dict[str, Any]:
        if order["payment_status"] != PaymentStatus.SUCCESS:
            raise APIException(status_code=400, error="invalid_order", detail="")

        refund_resp = self.gateway.refund(order["payment_info"]["rec_trade_id"])
        if refund_resp["status"] != 0:
            raise APIException(status_code=400, error="refund_failed", detail="")

        order = get_collection("order").find_one_and_update(
            {"_id": order["_id"]},
            {
                "$set": {
                    "payment_status": PaymentStatus.REFUNDED,
                    "refund_detail": refund_resp,
                }
            },
            return_document=True,
        )

        return order

    def token_request(
        self,
        cart: Cart,
        card_token: str,
        card_key: str,
    ) -> Dict[str, Any]:
        total = cart.total
        item_names = [item.product.name for item in cart.items]
        details = " | ".join(item_names)
        order_number = auto_order_number()

        checkout = cart.to_checkout(order_number=order_number)

        result_url = None
        resp = self.gateway.token_request(
            amount=total,
            order_number=order_number,
            details=details,
            card_key=card_key,
            card_token=card_token,
            card_ccv=None,
            three_domain_secure=False,
            result_url=result_url,
        )
        return self.handle_n3d_resp(checkout, resp)

    def prime_request(
        self,
        cart: Cart,
        prime: str,
        redirect_url: Optional[str] = None,
        callback_url: Optional[str] = None,
        cancel_url: Optional[str] = None,
    ) -> Dict[str, Any]:
        total = cart.total
        item_names = [item.product.name for item in cart.items]
        details = " | ".join(item_names)
        order_number = auto_order_number()

        checkout = cart.to_checkout(order_number=order_number)

        three_domain_secure = False
        result_url = None
        state_ins = get_collection("state")
        r = state_ins.insert_one({"state": str(uuid4())})

        if redirect_url is None:
            redirect_url = f"{SdkConfig.api_host}/payment/tappay/redirect"

        if callback_url is None:
            callback_url = f"{SdkConfig.api_host}/payment/tappay/callback?state={str(r.inserted_id)}"

        if cancel_url is None:
            cancel_url = SdkConfig.web_host

        if cart.payment_subtype == PaymentSubTypes.credit:
            three_domain_secure = True
            result_url = {
                "frontend_redirect_url": redirect_url,
                "backend_notify_url": callback_url,
                "go_back_url": cancel_url,
            }

        cardholder = {
            "phone_number": cart.buyer_phone,
            "name": cart.buyer_name,
            "email": cart.buyer_email,
        }

        resp = self.gateway.prime_request(
            amount=total,
            order_number=order_number,
            details=details,
            prime=prime,
            remember=True,
            three_domain_secure=three_domain_secure,
            result_url=result_url,
            cardholder=cardholder,
        )

        if cart.payment_subtype == PaymentSubTypes.credit:
            return self.handle_3d_resp(resp)

        else:
            return self.handle_n3d_resp(checkout, resp)

    def create_card_token(
        self,
        prime: str,
        card_holder: Dict[str, Any],
        redirect_url: str,
        callback_url: str,
        cancel_url: str,
    ) -> Dict[str, Any]:
        try:
            return self.gateway.bind_card(
                prime=prime,
                cardholder=card_holder,
                three_domain_secure=True,
                result_url={
                    "frontend_redirect_url": redirect_url,
                    "backend_notify_url": callback_url,
                    "go_back_url": cancel_url,
                },
            )
        except Exception as e:
            raise APIException(status_code=400, error="http_exception", detail=str(e))
