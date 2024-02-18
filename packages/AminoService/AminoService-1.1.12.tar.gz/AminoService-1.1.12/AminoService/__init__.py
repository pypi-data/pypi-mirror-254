__title__ = "AminoService"
__author__ = "innocentzero143"
__license__ = "MIT"
__copyright__ = "Copyright 2023-2024 innocentzero143"
__version__ = "1.1.12"

from .acm import ACM
from .client import Client
from .sub_client import SubClient
from .socket import Callbacks, SocketHandler

from .async_acm import AsyncACM
from .async_client import AsyncClient
from .async_sub_client import AsyncSubClient
from .async_socket import AsyncCallbacks, AsyncSocketHandler

from .lib.util import device, exceptions, headers, helpers, objects

from requests import get
from json import loads

__newest__ = loads(get("https://pypi.org/pypi/AminoService/json").text)["info"]["version"]
print(f"Lib Name = {__title__}")
print(f"Version = {__version__}")
print(f"Author Name = {__author__}")
if __version__ != __newest__:
    print(exceptions.LibraryUpdateAvailable(f"New version of {__title__} available: {__newest__} (Using {__version__})"))