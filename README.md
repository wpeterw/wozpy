#wozpy

[![codecov](https://codecov.io/gh/wpeterw/wozpy/graph/badge.svg?token=RZRGLN432W)](https://codecov.io/gh/wpeterw/wozpy)
[![Quality Gate Status](https://sonar.randombits.nl/api/project_badges/measure?project=wozpy&metric=alert_status&token=sqb_2339051b02256716cd52bed1a33d1065c76d0fef)](https://sonar.randombits.nl/dashboard?id=wozpy)
[![Maintainability](https://api.codeclimate.com/v1/badges/2a26fc9504ccd91cbf1d/maintainability)](https://codeclimate.com/github/wpeterw/wozpy/maintainability)

# Pythonpackage to get data from wozwaardeloket.nl

Install:

```
poetry add wozpy
```
Usage:

```
from wozpy import wozpy

wozpy.get_woz_value({"postcode": "3645AE", "house_number": "141", "house_number_extension": "d"}

```

Result:

```
[
    {
        "wozObject": {
            "wozobjectnummer": 73600001066,
            "woonplaatsnaam": "Vinkeveen",
            "openbareruimtenaam": "Baambrugse Zuwe",
            "straatnaam": "Baambrugse Zuwe",
            "postcode": "3645AE",
            "huisnummer": 141,
            "huisletter": "D",
            "huisnummertoevoeging": null,
            "locatieomschrijving": null,
            "gemeentecode": 736,
            "grondoppervlakte": 9905,
            "adresseerbaarobjectid": 736010000104061,
            "nummeraanduidingid": 736200000104061,
            "verbondenAdresseerbareObjecten": [
                736010000104061,
                736010000104220
            ],
            "ontleendeAdresseerbareObjecten": [
                736010000104061
            ]
        },
        "wozWaarden": [
            {
                "peildatum": "2022-01-01",
                "vastgesteldeWaarde": 16342000
            },
            {
                "peildatum": "2021-01-01",
                "vastgesteldeWaarde": 5383000
            },
            {
                "peildatum": "2020-01-01",
                "vastgesteldeWaarde": 3923000
            },
            {
                "peildatum": "2019-01-01",
                "vastgesteldeWaarde": 3741000
            },
            {
                "peildatum": "2018-01-01",
                "vastgesteldeWaarde": 3383000
            },
            {
                "peildatum": "2017-01-01",
                "vastgesteldeWaarde": 2249000
            },
            {
                "peildatum": "2016-01-01",
                "vastgesteldeWaarde": 1479000
            },
            {
                "peildatum": "2015-01-01",
                "vastgesteldeWaarde": 2237000
            },
            {
                "peildatum": "2014-01-01",
                "vastgesteldeWaarde": 2237000
            }
        ],
        "panden": [
            {
                "bagpandidentificatie": 736100000216431
            }
        ],
        "kadastraleObjecten": [
            {
                "kadastraleGemeenteCode": "VKV00",
                "kadastraleSectie": "A",
                "kadastraalPerceelNummer": "3744"
            },
            {
                "kadastraleGemeenteCode": "VKV00",
                "kadastraleSectie": "A",
                "kadastraalPerceelNummer": "4112"
            }
        ]
    }
]
```
