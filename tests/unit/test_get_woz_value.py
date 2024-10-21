import pytest
from unittest.mock import patch, Mock
import requests
from wozpy.wozpy import Wozpy
from wozpy.models.models import ModelItem


# Unit Tests
@pytest.fixture
def service():
    return Wozpy()


@patch.object(Wozpy, "_Wozpy__get_nummeraanduiding_id")
@patch("requests.get")
def test_get_woz_value_success(mock_get, mock_get_nummeraanduiding_id, service):
    # arrange
    mock_get_nummeraanduiding_id.return_value = ["id1", "id2"]

    # Create a mock response that matches the structure of ModelItem
    mock_response_1 = Mock()
    mock_response_1.json.return_value = {
        "wozObject": {
            "wozobjectnummer": 168000009999,
            "woonplaatsnaam": "Ons Dorp",
            "openbareruimtenaam": "Brin",
            "straatnaam": "Brink",
            "postcode": "9999AB",
            "huisnummer": 1,
            "huisletter": None,
            "huisnummertoevoeging": None,
            "locatieomschrijving": None,
            "gemeentecode": 9999,
            "grondoppervlakte": 900,
            "adresseerbaarobjectid": 1680010000000777,
            "nummeraanduidingid": 1680200000055555,
            "verbondenAdresseerbareObjecten": [1680010000000999],
            "ontleendeAdresseerbareObjecten": [1680010000000888],
        },
        "wozWaarden": [{"peildatum": "2023-01-01", "vastgesteldeWaarde": 492000}],
        "panden": [],
        "kadastraleObjecten": [
            {
                "kadastraleGemeenteCode": "ALO00",
                "kadastraleSectie": "Z",
                "kadastraalPerceelNummer": "1165",
            },
            {
                "kadastraleGemeenteCode": "ALO00",
                "kadastraleSectie": "Z",
                "kadastraalPerceelNummer": "1164",
            },
        ],
    }

    mock_response_2 = Mock()
    mock_response_2.json.return_value = {
        "wozObject": {
            "wozobjectnummer": 1680000022222,
            "woonplaatsnaam": "Ons Dorp",
            "openbareruimtenaam": "Brink",
            "straatnaam": "Brink",
            "postcode": "9999AB",
            "huisnummer": 1,
            "huisletter": None,
            "huisnummertoevoeging": None,
            "locatieomschrijving": None,
            "gemeentecode": 9999,
            "grondoppervlakte": 500,
            "adresseerbaarobjectid": 1680010000000383,
            "nummeraanduidingid": 1680200000011659,
            "verbondenAdresseerbareObjecten": [1680010000000383],
            "ontleendeAdresseerbareObjecten": [1680010000000383],
        },
        "wozWaarden": [{"peildatum": "2023-01-01", "vastgesteldeWaarde": 500000}],
        "panden": [],
        "kadastraleObjecten": [
            {
                "kadastraleGemeenteCode": "ALO00",
                "kadastraleSectie": "Z",
                "kadastraalPerceelNummer": "1166",
            }
        ],
    }

    mock_get.side_effect = [mock_response_1, mock_response_2]

    address = "Test Address"

    # act
    result = service.get_woz_value(address)

    # assert
    assert len(result) == 2  # Expecting two ModelItem instances
    assert isinstance(result[0], ModelItem)
    assert isinstance(result[1], ModelItem)
    assert result[0].woz_object.wozobjectnummer == 168000009999
    # assert result[1].woz_object.grondoppervlakte == 900
    assert result[1].woz_object.grondoppervlakte == 500
    assert result[0].woz_object.woonplaatsnaam == "Ons Dorp"
    assert result[0].woz_object.straatnaam == "Brink"
    assert result[1].woz_object.woonplaatsnaam == "Ons Dorp"
    assert result[1].woz_object.straatnaam == "Brink"
    mock_get_nummeraanduiding_id.assert_called_once_with(address)
    assert mock_get.call_count == 2


@patch.object(Wozpy, "_Wozpy__get_nummeraanduiding_id")
@patch("requests.get")
def test_get_woz_value_no_nummeraanduiding_ids(
    mock_get, mock_get_nummeraanduiding_id, service
):
    # arrange
    mock_get_nummeraanduiding_id.return_value = []

    address = "Test Address"

    # act
    result = service.get_woz_value(address)

    # assert
    assert result == []
    mock_get_nummeraanduiding_id.assert_called_once_with(address)
    mock_get.assert_not_called()


@patch.object(Wozpy, "_Wozpy__get_nummeraanduiding_id")
@patch("requests.get")
def test_get_woz_value_request_exception(
    mock_get, mock_get_nummeraanduiding_id, service
):
    # arrange
    mock_get_nummeraanduiding_id.return_value = ["id1"]
    mock_get.side_effect = requests.RequestException("API request failed")

    address = "Test Address"

    # act & assert
    with pytest.raises(requests.RequestException, match="API request failed"):
        service.get_woz_value(address)

    mock_get_nummeraanduiding_id.assert_called_once_with(address)
    mock_get.assert_called_once()
