import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

SECRET_KEY = os.environ.get("SECRET_KEY")
TOKEN_DURATION_MINUTES = int(os.environ.get("TOKEN_DURATION_MINUTES"))
