from unittest.mock import Mock, patch

from wozpy.wozpy import wozpy


class TestWozpy:
    @patch("requests.post")
    def test_get_cookie_success(self, mock_post):
        # Mocking the requests.post method to return a response with cookies
        mock_response = Mock()
        mock_response.cookies.get_dict.return_value = {"mock_cookie": "mock_value"}
        mock_post.return_value = mock_response

        wozpy_instance = wozpy
        result = wozpy_instance._Wozpy__get_cookie()

        assert result == {"mock_cookie": "mock_value"}
        result = wozpy_instance._Wozpy__get_cookie()

        assert result == {"mock_cookie": "mock_value"}

    def test_get_woz_address_id_success(self):
        address = "3645AE 141D"
        result = wozpy._Wozpy__get_woz_address_id(address)
        assert result == ["adr-53c3d765a99c3d43cd02d777f13aee86"]

    def test_get_nummeraanduiding_id_success(self):
        address = "3645AE 141D"
        result = wozpy._Wozpy__get_nummeraanduiding_id(address)
        assert result == ["0736200000104061"]

    def test_get_nummeraanduiding_id_request_error(self):
        address = "Vinkeveen"
        result = wozpy._Wozpy__get_nummeraanduiding_id(address)
        assert result == []
