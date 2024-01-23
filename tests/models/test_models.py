import pytest
from pydantic import ValidationError

from wozpy.models.models import Address


class TestModels:
    def test_address_full_address(self):
        address_data = {
            "postcode": "1234AB",
            "house_number": "42",
            "house_number_extension": "A",
        }
        address = Address(**address_data)

        assert address.full_address == "1234AB 42 A"

    def test_address_full_address_without_extension(self):
        address_data = {"postcode": "5678CD", "house_number": "99"}
        address = Address(**address_data)

        assert address.full_address == "5678CD 99"

    def test_dutch_postcode_valid(self):
        valid_postcodes = ["1234 AB", "5678CD"]
        for postcode in valid_postcodes:
            address_data = {"postcode": postcode, "house_number": "42"}
            address = Address(**address_data)
            assert address.postcode == postcode

    def test_dutch_postcode_invalid(self):
        invalid_postcodes = ["12AB CD", "1234", "12345 AB"]
        for postcode in invalid_postcodes:
            with pytest.raises(ValidationError):
                address_data = {"postcode": postcode, "house_number": "42"}
                Address(**address_data)
                Address(**address_data)
