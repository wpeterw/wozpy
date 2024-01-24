import re
from typing import Optional

from pydantic import BaseModel, field_validator


class Address(BaseModel):
    postcode: str
    house_number: str
    house_number_extension: Optional[str] = None

    @property
    def full_address(self) -> str:
        """Returns a concatenation of postcode, space, house_number, and house_number_extension."""
        address_parts = [self.postcode, self.house_number]
        if self.house_number_extension:
            address_parts.append(self.house_number_extension)
        return " ".join(address_parts)

    @field_validator("postcode")
    def dutch_postcode(cls, v):
        if not re.match("^\d{4}\s?\w{2}$", v):
            raise ValueError("must follow regex ^\d{4}\s?\w{2}$")
        return v
