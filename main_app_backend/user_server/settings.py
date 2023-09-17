import os
from dotenv import load_dotenv, find_dotenv
import logging

load_dotenv(find_dotenv())

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename='user_server.log',
                    datefmt='%Y-%m-%d %H:%M:%S')

SECRET_KEY = os.environ.get("SECRET_KEY")
DATABASE_URL = os.environ.get("DATABASE_URL")
