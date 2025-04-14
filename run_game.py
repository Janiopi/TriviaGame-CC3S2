from app.run_quiz import run_quiz
from app.db.db_connection import create_connection_pool

# Crear el pool de conexiones al iniciar la aplicación
create_connection_pool()
# Iniciar el juego de trivia

if __name__ == "__main__":
    run_quiz()
