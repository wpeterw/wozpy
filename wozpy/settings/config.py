from pydantic_settings import BaseSettings


class Config(BaseSettings):
    pdok_base_url: str = "https://api.pdok.nl/bzk/locatieserver/search/v3_1/lookup"
    woz_base_url: str = "https://www.wozwaardeloket.nl/wozwaardeloket-api/v1/wozwaarde/nummeraanduiding/"
    cookie_url: str = (
        "https://www.wozwaardeloket.nl/wozwaardeloket-api/v1/session/start"
    )
