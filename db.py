import os
import mysql.connector
from dotenv import load_dotenv

# Carga variables de .env
load_dotenv()

# Lee las variables de entorno para la BD
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

def get_connection():
    """Devuelve una conexión a la BD MySQL."""
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        return conn
    except Exception as e:
        raise RuntimeError(f"Error conectando a MySQL: {str(e)}")
