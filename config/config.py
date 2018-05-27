import os
from dotenv import load_dotenv
from pathlib import Path  # python3 only
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


load_dotenv()

class APPLICATIONCONFIG(object):
    DATABASE = 'flaskr.db'
    DEBUG = True
    SECRET_KEY = 'my_precious'
    USERNAME = 'admin'
    PASSWORD = 'admin'
