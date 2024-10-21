from typing import Any

from pydantic import BaseModel, Field


class WozObject(BaseModel):
    wozobjectnummer: int
    woonplaatsnaam: str
    openbareruimtenaam: str
    straatnaam: str
    postcode: str
    huisnummer: int
    huisletter: str | None = None
    huisnummertoevoeging: Any | None = None
    locatieomschrijving: str | None = None 
    gemeentecode: int
    grondoppervlakte: int
    adresseerbaarobjectid: int
    nummeraanduidingid: int
    verbonden_adresseerbare_objecten: list[int] = Field(
        ..., alias='verbondenAdresseerbareObjecten'
    )
    ontleende_adresseerbare_objecten: list[int] = Field(
        ..., alias='ontleendeAdresseerbareObjecten'
    )


class WozWaardenItem(BaseModel):
    peildatum: str
    vastgestelde_waarde: int = Field(..., alias='vastgesteldeWaarde')


class KadastraleObjectenItem(BaseModel):
    kadastrale_gemeente_code: str = Field(..., alias='kadastraleGemeenteCode')
    kadastrale_sectie: str = Field(..., alias='kadastraleSectie')
    kadastraal_perceel_nummer: str = Field(..., alias='kadastraalPerceelNummer')


class ModelItem(BaseModel):
    woz_object: WozObject = Field(..., alias='wozObject')
    woz_waarden: list[WozWaardenItem] = Field(..., alias='wozWaarden')
    panden: list
    kadastrale_objecten: list[KadastraleObjectenItem] = Field(
        ..., alias='kadastraleObjecten'
    )
