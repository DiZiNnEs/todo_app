from os import getenv
from dotenv import load_dotenv

load_dotenv()


def env(key: str) -> str:
    value = getenv(key)
    if value is None:
        raise EnvironmentError(f'No key {key} in .env file')
    return value
