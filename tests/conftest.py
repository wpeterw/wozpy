from unittest.mock import Mock

import pytest


@pytest.fixture
def mock_settings(self):
    return Mock(cookie_url="https://example.com/cookie")
