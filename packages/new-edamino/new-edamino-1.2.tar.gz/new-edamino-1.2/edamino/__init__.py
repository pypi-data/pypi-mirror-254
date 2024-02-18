from .client import Client
from .bot import Bot
from .context import Context
from .logger import logger
from requests import get
from json import loads

__version__ = '1.2'

__newest__ = loads(get("https://pypi.org/pypi/new-edamino/json").text)["info"]["version"]

if __version__ != __newest__:
    print(f"New version available: {__newest__} (Using {__version__})")
    print("Talk in discord like 「𝑴𝑶𝑵𝑺𝑻𝑬𝑹」#4545")
