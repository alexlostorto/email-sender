# Relative files
import os

# Environment variables
from dotenv import load_dotenv


def getCredentials():
    load_dotenv()
    appKey = os.getenv('APPKEY')

    return appKey
