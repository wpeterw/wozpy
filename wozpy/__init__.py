#  __          ______ _____________     __
#  \ \        / / __ \___  /  __ \ \   / /
#   \ \  /\  / / |  | | / /| |__) \ \_/ /
#    \ \/  \/ /| |  | |/ / |  ___/ \   /
#     \  /\  / | |__| / /__| |      | |
#      \/  \/   \____/_____|_|      |_|

"""
Unofficial Python wrapper for the Wozwaardeloket API.
~~~~~~~~~~~~~~~~~~~~~

Basic usage:

   >>> import wozpy
   >>> r = requests.get('https://www.python.org')
   >>> 
   >>> 
"""
import logging
from logging import NullHandler

logging.getLogger(__name__).addHandler(NullHandler())
