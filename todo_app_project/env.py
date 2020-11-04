from os import getenv
from dotenv import load_dotenv

load_dotenv()


def env(key: str) -> str:
    value = getenv(key)
    if value is None:
        raise EnvironmentError('Key with this name was not found in the file .env')
    return value
