from fastapi import FastAPI
from app.db.db_connection import create_connection_pool
from app.db.db_queries import get_questions_by_difficulty

app = FastAPI()

#Inicializando el pool de conexiones
create_connection_pool()


@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API de Trivia!"}


@app.get("/questions/{difficulty}")
def get_questions(difficulty: str):
    """
    Endpoint para obtener preguntas de trivia según la dificultad.
    :param difficulty: Dificultad de las preguntas (fácil, media, difícil).
    :return: Lista de preguntas en formato JSON.
    """
    # Aquí deberías llamar a tu función que obtiene las preguntas de la base de datos
    questions = get_questions_by_difficulty(difficulty)
    
    if not questions:
        return {"message": "No se encontraron preguntas para esta dificultad."}
    
    return {"questions": [question.__dict__ for question in questions]}





