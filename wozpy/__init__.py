#  __          ______ _____________     __
#  \ \        / / __ \___  /  __ \ \   / /
#   \ \  /\  / / |  | | / /| |__) \ \_/ /
#    \ \/  \/ /| |  | |/ / |  ___/ \   /
#     \  /\  / | |__| / /__| |      | |
#      \/  \/   \____/_____|_|      |_|

"""
Unofficial Python wrapper for the unofficial Wozwaardeloket API. So, pretty unofficial.
~~~~~~~~~~~~~~~~~~~~~

Basic usage:

   >>> from wozpy.woz import woz
   >>> woz = woz.get_woz_value({"postcode": "3645AE", "house_number": "141", "house_number_extension": "D"})
   >>> 
   >>> 
"""
import logging
from logging import NullHandler

logging.getLogger(__name__).addHandler(NullHandler())
