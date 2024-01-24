from unittest.mock import Mock, patch

import requests_mock

from wozpy.woz import woz


class TestWozpy:
    @patch("requests.post")
    def test_get_cookie_success(self, mock_post):
        # Mocking the requests.post method to return a response with cookies
        mock_response = Mock()
        mock_response.cookies.get_dict.return_value = {"mock_cookie": "mock_value"}
        mock_post.return_value = mock_response

        wozpy_instance = woz
        result = wozpy_instance._Wozpy__get_cookie()

        assert result == {"mock_cookie": "mock_value"}
        result = wozpy_instance._Wozpy__get_cookie()

        assert result == {"mock_cookie": "mock_value"}

    def test_get_woz_address_id_success(self):
        address = "3645AE 141D"
        result = woz._Wozpy__get_woz_address_id(address)
        assert result == ["adr-53c3d765a99c3d43cd02d777f13aee86"]

    def test_get_nummeraanduiding_id_success(self):
        address = "3645AE 141D"
        result = woz._Wozpy__get_nummeraanduiding_id(address)
        assert result == ["0736200000104061"]

    def test_get_nummeraanduiding_id_request_error(self):
        address = "Vinkeveen"
        result = woz._Wozpy__get_nummeraanduiding_id(address)
        assert result == []

    def test_get_woz_value_success(self):
        address_data = {
            "postcode": "3645AE",
            "house_number": "141",
            "house_number_extension": "D",
        }

        # Mock the requests.get method to return a predefined response
        with requests_mock.Mocker() as m:
            m.get(
                requests_mock.ANY, json={"wozObject": {"wozobjectnummer": 73600001066}}
            )

            # Mock the __get_nummeraanduiding_id method to return a predefined value
            with patch.object(
                woz, "_Wozpy__get_nummeraanduiding_id", return_value=["123", "456"]
            ):
                result = woz.get_woz_value(address_data)

        wozobjectnummer = result[0].get("wozObject").get("wozobjectnummer")
        assert wozobjectnummer == 73600001066
