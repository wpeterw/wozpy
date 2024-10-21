from typing import Any
import requests
import logging
from .models.models import ModelItem
from pydantic import ValidationError
logger = logging.getLogger(__name__)


class Wozpy:
    def __get_woz_address_id(self, address: str) -> list[str] | None:
        """
        Retrieve the WOZ address ID(s) from the WOZ web service.

        Args:
            address (str): The address for which to retrieve WOZ address ID(s).

        Returns:
            Optional[List[str]]: A list of WOZ address ID(s) if found, otherwise `None`.
        """
        quoted_address = f'"{address}"'
        url = "https://api.pdok.nl/bzk/locatieserver/search/v3_1/suggest"
        params = {"q": quoted_address}

        try:
            response = requests.get(url, params=params, timeout=5)
            response.raise_for_status()
            data = response.json()

            # Extract and return the list of IDs from the response
            return [
                doc.get("id", "") for doc in data.get("response", {}).get("docs", [])
            ]

        except (requests.RequestException, ValueError, KeyError, IndexError) as ex:
            logger.error(
                f"Error while retrieving or parsing address ID from WOZ web service: {ex}"
            )
            return None

    def __get_nummeraanduiding_id(self, address: str) -> list[Any] | None:
        """
        Retrieve the `nummeraanduiding_id` from the WOZ web service for a given address.

        Args:
            address (str): The address for which to retrieve the `nummeraanduiding_id`.

        Returns:
            Optional[list[Any]]: A list of `nummeraanduiding_id` values if found, otherwise `None`.
        """
        _ids = self.__get_woz_address_id(address)
        url = "https://api.pdok.nl/bzk/locatieserver/search/v3_1/lookup"

        if not _ids:
            logger.error(f"No WOZ address ID found for {address}")
            return None

        nummeraanduiding_ids = []

        for _id in _ids:
            try:
                data = self.__fetch_nummeraanduiding_data(url, _id)
                nummeraanduiding_id = (
                    data.get("response", {})
                    .get("docs", [{}])[0]
                    .get("nummeraanduiding_id")
                )
                if nummeraanduiding_id:
                    nummeraanduiding_ids.append(nummeraanduiding_id)
            except Exception as ex:
                logger.error(
                    f"Error fetching nummeraanduiding_id for WOZ address ID {_id}: {ex}"
                )

        if not nummeraanduiding_ids:
            logger.warning(f"No nummeraanduiding_ids found for {address}")

        return nummeraanduiding_ids

    def __fetch_nummeraanduiding_data(self, url: str, _id: str) -> dict:
        """Helper method to fetch nummeraanduiding data for a given WOZ address ID."""
        params = {"id": _id}
        try:
            response = requests.get(url=url, params=params, timeout=5)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logger.error(f"Request failed for {_id} with error: {e}")
            return {}

    def get_woz_value(self, address: str) -> list[ModelItem]:
        """
        Get the WOZ (Waardering Onroerende Zaken) information for wozwaardeloket.nl.

        Args:
            address (str): A string representing the address information.
                Example: 1000AB Dam 1 Amsterdam or 1000AB Dam 2A Amsterdam

        Returns:
            List[ModelItem]: A list of Pydantic models containing the WOZ information for the specified address.
                            Each model represents information for a specific WOZ object.

        Raises:
            requests.exceptions.RequestException: If there is an issue with the HTTP request to wozwaardeloket.nl.
            ValidationError: If the provided address does not adhere to the expected structure.
        """
        nummeraanduiding_ids = self.__get_nummeraanduiding_id(address)
        base_url = "https://api.kadaster.nl/lvwoz/wozwaardeloket-api/v1/wozwaarde/nummeraanduiding/"

        if not nummeraanduiding_ids:
            return []

        results = []
        
        for nummeraanduiding_id in nummeraanduiding_ids:
            try:
                response = requests.get(f"{base_url}{nummeraanduiding_id}", timeout=5)
                response.raise_for_status()
                data = response.json()

                # Validate and create Pydantic model instance
                model_item = ModelItem(**data)
                results.append(model_item)

            except requests.exceptions.RequestException as e:
                raise e
            except ValidationError as e:
                logger.error(f"Validation error for data: {data}, error: {e}")
                continue

        return results
