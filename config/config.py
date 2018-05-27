import os
from dotenv import load_dotenv
from pathlib import Path  # python3 only
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


load_dotenv()

# get the project base directory
basedir = os.path.abspath('')

# database config
class APPLICATIONCONFIG(object):
    DATABASE = 'flaskr.db'
    DEBUG = True
    SECRET_KEY = 'my_precious'
    USERNAME = 'admin'
    PASSWORD = 'admin'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, DATABASE)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
