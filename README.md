#wozpy

[![codecov](https://codecov.io/gh/wpeterw/wozpy/graph/badge.svg?token=RZRGLN432W)](https://codecov.io/gh/wpeterw/wozpy)
[![Quality Gate Status](https://sonar.randombits.nl/api/project_badges/measure?project=wozpy&metric=alert_status&token=sqb_2339051b02256716cd52bed1a33d1065c76d0fef)](https://sonar.randombits.nl/dashboard?id=wozpy)
[![Maintainability](https://api.codeclimate.com/v1/badges/2a26fc9504ccd91cbf1d/maintainability)](https://codeclimate.com/github/wpeterw/wozpy/maintainability)
![Workflow](https://github.com/wpeterw/wozpy/actions/workflows/build_and_test.yaml/badge.svg)
[![PyPI version](https://badge.fury.io/py/wozpy.svg)](https://badge.fury.io/py/wozpy)

# Pythonpackage to get data from wozwaardeloket.nl

Install:

```
poetry add wozpy
or if you must:
pip install wozpy
```
Usage:

```
from wozpy.wozpy import Wozpy
woz = Wozpy()
woz_value = woz.get_woz_value("Logosberg 3 1251GL Laren")

```

Result:

```
This returns a pydantic object.

Example:

for model_item in woz_value:
    print(f"WOZ Object Number: {model_item.woz_object.wozobjectnummer}")
    print(f"Place Name: {model_item.woz_object.woonplaatsnaam}")
    print(f"Street Name: {model_item.woz_object.straatnaam}")
    
    for woz_waarde in model_item.woz_waarden:
        print(f"Peildatum: {woz_waarde.peildatum}, Vastgestelde Waarde: {woz_waarde.vastgestelde_waarde}")

```
Will print:

WOZ Object Number: 41700002562
Place Name: Laren
Street Name: Logosberg
Peildatum: 2023-01-01, Vastgestelde Waarde: 25141000
Peildatum: 2022-01-01, Vastgestelde Waarde: 18296000
Peildatum: 2021-01-01, Vastgestelde Waarde: 15789000
Peildatum: 2020-01-01, Vastgestelde Waarde: 16332000
Peildatum: 2019-01-01, Vastgestelde Waarde: 15240000
Peildatum: 2018-01-01, Vastgestelde Waarde: 15459000
Peildatum: 2017-01-01, Vastgestelde Waarde: 14941000
Peildatum: 2016-01-01, Vastgestelde Waarde: 14823000
Peildatum: 2015-01-01, Vastgestelde Waarde: 14392000
Peildatum: 2014-01-01, Vastgestelde Waarde: 14343000
