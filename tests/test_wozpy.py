from unittest.mock import Mock, patch

import pytest

from wozpy.wozpy import wozpy  # Adjust the import path based on your project structure


class TestWozpy:
    @pytest.fixture
    def mock_settings(self):
        return Mock(cookie_url="http://example.com/cookie")

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
