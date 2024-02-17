from typing import Any, Dict, Optional

import requests


class TappayGateway:
    @property
    def url(self) -> str:
        if self.stage in ["prod", "PROD"]:
            return "https://prod.tappaysdk.com/tpc"
        return "https://sandbox.tappaysdk.com/tpc"

    def __init__(self, partner_key: str, merchant_id: str, stage: str):
        self.partner_key = partner_key
        self.merchant_id = merchant_id
        self.stage = stage

    def build_headers(self) -> Dict[str, Any]:
        return {"Content-Type": "application/json", "x-api-key": self.partner_key}

    def prime_request(
        self,
        amount: int,
        order_number: str,
        details: str,
        prime: str,
        cardholder: Dict[str, Any],
        three_domain_secure: bool,
        result_url: Optional[Dict[str, Any]] = None,
        currency: str = "TWD",
        remember: bool = True,
    ) -> Dict[str, Any]:
        endpoint = f"{self.url}/payment/pay-by-prime"
        body = {
            "partner_key": self.partner_key,
            "merchant_id": self.merchant_id,
            "amount": amount,
            "order_number": order_number,
            "details": details,
            "prime": prime,
            "cardholder": cardholder,
            "three_domain_secure": three_domain_secure,
            "result_url": result_url,
            "currency": currency,
            "remember": remember,
        }
        headers = self.build_headers()
        res = requests.post(url=endpoint, json=body, headers=headers)
        res.raise_for_status()
        res_json = res.json()
        assert isinstance(res_json, dict)
        return res_json

    def token_request(
        self,
        amount: int,
        order_number: str,
        details: str,
        card_key: str,
        card_token: str,
        card_ccv: Optional[str],
        three_domain_secure: bool,
        result_url: Optional[Dict[str, Any]] = None,
        currency: str = "TWD",
        remember: bool = True,
    ) -> Dict[str, Any]:
        endpoint = f"{self.url}/payment/pay-by-token"
        body = {
            "partner_key": self.partner_key,
            "merchant_id": self.merchant_id,
            "amount": amount,
            "order_number": order_number,
            "details": details,
            "card_key": card_key,
            "card_token": card_token,
            "card_ccv": card_ccv,
            "three_domain_secure": three_domain_secure,
            "result_url": result_url,
            "currency": currency,
            "remember": remember,
        }
        headers = self.build_headers()
        res = requests.post(url=endpoint, json=body, headers=headers)
        res.raise_for_status()
        res_json = res.json()
        assert isinstance(res_json, dict)
        return res_json

    def get_record(self, rec_trade_id: str, order_number: str) -> Dict[str, Any]:
        endpoint = f"{self.url}/transaction/query"
        request_body = {
            "partner_key": self.partner_key,
            "records_per_page": 10,
            "page": 0,
            "filters": {"rec_trade_id": rec_trade_id, "order_number": order_number},
        }
        headers = self.build_headers()
        res = requests.post(url=endpoint, json=request_body, headers=headers)
        res.raise_for_status()
        res_json = res.json()
        assert isinstance(res_json, dict)
        return res_json

    def refund(self, rec_trade_id: str) -> Dict[str, Any]:
        endpoint = f"{self.url}/transaction/refund"
        body = {
            "partner_key": self.partner_key,
            "rec_trade_id": rec_trade_id,
        }
        resp = requests.post(url=endpoint, json=body, headers=self.build_headers())
        resp.raise_for_status()
        resp_json = resp.json()
        return resp_json  # type: ignore

    def bind_card(
        self,
        prime: str,
        cardholder: Dict[str, Any],
        three_domain_secure: bool,
        result_url: Optional[Dict[str, Any]] = None,
        currency: str = "TWD",
        cardholder_verify: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        endpoint = f"{self.url}/tpc/card/bind"
        body = {
            "partner_key": self.partner_key,
            "merchant_id": self.merchant_id,
            "prime": prime,
            "cardholder": cardholder,
            "three_domain_secure": three_domain_secure,
            "result_url": result_url,
            "currency": currency,
            "cardholder_verify": cardholder_verify,
        }
        headers = self.build_headers()
        res = requests.post(url=endpoint, json=body, headers=headers)
        res.raise_for_status()
        res_json = res.json()
        assert isinstance(res_json, dict)
        return res_json
