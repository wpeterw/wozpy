import pytest
from unittest.mock import patch, Mock
from wozpy.wozpy import Wozpy
import requests

@pytest.fixture
def service():
    return Wozpy()

@patch('requests.get')
def test_get_woz_address_id_success(mock_get, service):
    # Mock a successful response
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "response": {
            "docs": [{"id": "1234"}, {"id": "5678"}]
        }
    }
    mock_get.return_value = mock_response

    address = "Test Address"
    result = service._Wozpy__get_woz_address_id(address)

    assert result == ["1234", "5678"]
    mock_get.assert_called_once_with(
        "https://api.pdok.nl/bzk/locatieserver/search/v3_1/suggest", params={'q': '"Test Address"'}, timeout=5
    )

@patch('requests.get')
def test_get_woz_address_id_empty_response(mock_get, service):
    # arrange
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "response": {
            "docs": []
        }
    }
    mock_get.return_value = mock_response

    # act
    address = "Test Address"
    result = service._Wozpy__get_woz_address_id(address)
    
    # assert
    assert result == []
    mock_get.assert_called_once()

@patch('requests.get')
def test_get_woz_address_id_request_exception(mock_get, service):
    # arrange
    mock_get.side_effect = requests.RequestException("API error")
    address = "Test Address"

    # act
    result = service._Wozpy__get_woz_address_id(address)

    # assert
    assert result is None
    mock_get.assert_called_once()

@patch('requests.get')
def test_get_woz_address_id_value_error(mock_get, service):
    # arrange
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.side_effect = ValueError("JSON parsing error")
    mock_get.return_value = mock_response

    address = "Test Address"
    
    # act
    result = service._Wozpy__get_woz_address_id(address)

    # assert
    assert result is None
    mock_get.assert_called_once()