import os

import requests
from dotenv import load_dotenv

from models.requestDto.requestDto import RequestDto


load_dotenv()


class ApiCaller:

    BASE_URL = "https://api.coingecko.com/api/v3"

    def __init__(self):

        self.api_key = os.getenv("COINGECKO_API_KEY")

        if not self.api_key:
            raise ValueError(
                "COINGECKO_API_KEY no está configurada"
            )

    def call(self, request: RequestDto):

        if not isinstance(request, RequestDto):
            raise TypeError(
                "request debe ser una instancia de RequestDto"
            )

        url = request.get_url(self.BASE_URL)

        headers = {
            "accept": "application/json",
            "x-cg-demo-api-key": self.api_key
        }

        response = requests.request(
            method=request.method,
            url=url,
            headers=headers,
            params=request.get_query_params(),
            timeout=30
        )

        response.raise_for_status()

        return response.json()
