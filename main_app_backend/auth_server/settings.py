import os
from dotenv import load_dotenv, find_dotenv
import logging

load_dotenv(find_dotenv())

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename='auth_server.log',
                    datefmt='%Y-%m-%d %H:%M:%S')

SECRET_KEY = os.environ.get("SECRET_KEY")
TOKEN_DURATION_MINUTES = int(os.environ.get("TOKEN_DURATION_MINUTES"))
REDIS_HOST = os.environ.get("REDIS_HOST")
REDIS_PORT = os.environ.get("REDIS_PORT")
