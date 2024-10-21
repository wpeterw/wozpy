import pytest
from unittest.mock import patch, Mock
import requests
from wozpy.wozpy import Wozpy


@pytest.fixture
def service():
    return Wozpy()


@patch("requests.get")
def test_fetch_nummeraanduiding_data_success(mock_get, service):
    # arrange
    mock_response = Mock()
    mock_response.json.return_value = {
        "response": {"docs": [{"nummeraanduiding_id": "num1"}]}
    }
    mock_response.status_code = 200
    mock_get.return_value = mock_response

    url = "https://example.com"
    _id = "test_id"

    # act
    result = service._Wozpy__fetch_nummeraanduiding_data(url, _id)

    # assert
    assert result == {"response": {"docs": [{"nummeraanduiding_id": "num1"}]}}
    mock_get.assert_called_once_with(url=url, params={"id": _id}, timeout=5)


@patch("requests.get")
def test_fetch_nummeraanduiding_data_request_exception(mock_get, service):
    # arrange
    mock_get.side_effect = requests.RequestException("Request failed")

    url = "https://example.com"
    _id = "test_id"

    # act
    result = service._Wozpy__fetch_nummeraanduiding_data(url, _id)

    # assert
    assert result == {}  # Should return an empty dictionary on failure
    mock_get.assert_called_once_with(url=url, params={"id": _id}, timeout=5)
