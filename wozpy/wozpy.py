import logging
from typing import Any

import requests
from requests.exceptions import RequestException

from .settings import config


class Wozpy:
    def __init__(self, settings):
        self.settings = settings
        self.cookie = self.__get_cookie()

    def __get_cookie(self, timeout=5) -> dict | None:
        """Get a cookie for the WOZ web service."""
        url = self.settings.cookie_url
        try:
            response = requests.post(url=url, timeout=timeout)
            # x = response.cookies.get_dict()
            response.raise_for_status()
            return response.cookies.get_dict()
        except RequestException as exception:
            logging.exception(
                "Error while getting cookie from wozwaardeloket.nl: %s", exception
            )
            return None

    def __get_woz_address_id(self, address: str) -> list[str] | None:
        """Get the WOZ address ID from the WOZ web service."""
        url = "https://api.pdok.nl/bzk/locatieserver/search/v3_1/suggest"
        params = {"q": address}
        try:
            response = requests.get(url, params=params, timeout=5)
            response.raise_for_status()
            data = response.json()

            return [
                doc.get("id", "") for doc in data.get("response", {}).get("docs", [])
            ]

        except requests.exceptions.RequestException as ex:
            logging.error("Error while getting address ID from WOZ web service: %s", ex)
            return None
        except (ValueError, KeyError, IndexError) as ex:
            logging.error("Error while parsing response: %s", ex)
            return None

    def __get_nummeraanduiding_id(self, address: str) -> list[Any]:
        """Get the nummeraanduiding_id from the WOZ web service."""
        _ids = self.__get_woz_address_id(address)
        url = self.settings.pdok_base_url

        if _ids:
            nummeraanduiding_ids = []
            for _id in _ids:
                params = {"id": _id}
                response = requests.get(url=url, params=params, timeout=5)
                response.raise_for_status()
                data = response.json()
                nummeraanduiding_id = (
                    data.get("response", {})
                    .get("docs", [{}])[0]
                    .get("nummeraanduiding_id")
                )
                if nummeraanduiding_id:
                    nummeraanduiding_ids.append(nummeraanduiding_id)

        return nummeraanduiding_ids

    def get_woz_value(self, address: str) -> list[dict]:
        """Get the WOZ information for wozwaardeloket.nl"""
        results = []

        nummeraanduiding_ids = self.__get_nummeraanduiding_id(address)
        headers = {
            "Cookie": f"LB_STICKY={self.cookie.get('LB_STICKY')}; SESSION={self.cookie.get('SESSION')}"
        }

        for nummeraanduiding_id in nummeraanduiding_ids:
            url = f"{self.settings.woz_base_url}{nummeraanduiding_id}"

            response = requests.get(url=url, headers=headers, timeout=5).json()
            results.append(response)
        return results


wozpy = Wozpy(config.Config())
wozpy = Wozpy(config.Config())
wozpy = Wozpy(config.Config())
