import pytest
from unittest.mock import patch
from wozpy.wozpy import Wozpy

# Tests
@pytest.fixture
def service():
    return Wozpy()

@patch.object(Wozpy, '_Wozpy__get_woz_address_id')
@patch.object(Wozpy, '_Wozpy__fetch_nummeraanduiding_data')
def test_get_nummeraanduiding_id_success(mock_fetch_data, mock_get_woz_id, service):
    # arrange
    mock_get_woz_id.return_value = ["id1", "id2"]

    mock_fetch_data.side_effect = [
        {"response": {"docs": [{"nummeraanduiding_id": "num1"}]}},
        {"response": {"docs": [{"nummeraanduiding_id": "num2"}]}}
    ]

    address = "Test Address"

    # act
    result = service._Wozpy__get_nummeraanduiding_id(address)

    # assert
    assert result == ["num1", "num2"]
    mock_get_woz_id.assert_called_once_with(address)
    assert mock_fetch_data.call_count == 2

@patch.object(Wozpy, '_Wozpy__get_woz_address_id')
def test_get_nummeraanduiding_id_no_ids(mock_get_woz_id, service):
    # arrange
    mock_get_woz_id.return_value = None

    address = "Test Address"
    
    # act
    result = service._Wozpy__get_nummeraanduiding_id(address)

    # assert
    assert result is None
    mock_get_woz_id.assert_called_once_with(address)

@patch.object(Wozpy, '_Wozpy__get_woz_address_id')
@patch.object(Wozpy, '_Wozpy__fetch_nummeraanduiding_data')
def test_get_nummeraanduiding_id_no_nummeraanduiding_ids(mock_fetch_data, mock_get_woz_id, service):
    # arrange
    mock_get_woz_id.return_value = ["id1"]
    mock_fetch_data.return_value = {"response": {"docs": [{}]}}

    address = "Test Address"

    # act
    result = service._Wozpy__get_nummeraanduiding_id(address)

    # assert
    assert result == []
    mock_get_woz_id.assert_called_once_with(address)
    mock_fetch_data.assert_called_once()

@patch.object(Wozpy, '_Wozpy__get_woz_address_id')
@patch.object(Wozpy, '_Wozpy__fetch_nummeraanduiding_data')
def test_get_nummeraanduiding_id_error_handling(mock_fetch_data, mock_get_woz_id, service):
    # arrange
    mock_get_woz_id.return_value = ["id1"]
    mock_fetch_data.side_effect = Exception("Data fetch error")

    address = "Test Address"

    # act
    result = service._Wozpy__get_nummeraanduiding_id(address)

    # assert
    assert result == []
    mock_get_woz_id.assert_called_once_with(address)
    mock_fetch_data.assert_called_once()
