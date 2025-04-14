import psycopg2
from psycopg2 import pool
import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Crear el pool de conexiones al iniciar la aplicación
connection_pool = None

def create_connection_pool():
    """Crea el pool de conexiones solo una vez."""
    global connection_pool
    try:
        # Configurar las credenciales de la BD (usando variables de entorno)
        host = os.getenv("DB_HOST", "localhost")
        database = os.getenv("DB_NAME", "trivia_db")
        user = os.getenv("DB_USER", "trivia_user")
        password = os.getenv("DB_PASSWORD", "trivia_pass")

        connection_pool = psycopg2.pool.SimpleConnectionPool(
            1,  # Mínimo número de conexiones en el pool
            10, # Máximo número de conexiones en el pool
            host=host,
            database=database,
            user=user,
            password=password
        )
        # print("Pool de conexiones creado exitosamente.")
    except Exception as e:
        print(f"Error al crear el pool de conexiones: {e}")


def get_connection_from_pool():
    """Obtiene una conexión del pool, si está disponible."""
    if connection_pool:
        return connection_pool.getconn()
    else:
        print("Error: El pool de conexiones no está inicializado.")
        return None


def release_connection_to_pool(conn):
    """Libera una conexión al pool."""
    if connection_pool and conn:
        connection_pool.putconn(conn)
