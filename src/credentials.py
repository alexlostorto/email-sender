# Relative files
import os

# Environment variables
from dotenv import load_dotenv


def getCredentials():
    load_dotenv()
    appKey = os.getenv('APPKEY')

    if appKey == None:
        raise ValueError("[ERROR] No APPKEY found in .env")

    return appKey
