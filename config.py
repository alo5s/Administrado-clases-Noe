import os
from dotenv import load_dotenv
# Carga las variables de entorno desde el archivo .env
load_dotenv()

class Config:
    SECRET_KEY =  os.environ.get('SECRET_KET_FLASK')
    #localhost:8000
    #SERVER_NAME = "localhost:8000"
    SERVER_NAME = "127.0.0.1:8000"
    DEBUG = True
    
    TEMPLATE_FOLDER = "views/templates/"
    STATIC_FOLDER = "views/static/"
