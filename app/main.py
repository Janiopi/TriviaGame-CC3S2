from fastapi import FastAPI
from app.db.db_connection import create_connection_pool
from app.db.db_queries import get_all_questions
from app.run_quiz import run_quiz
import threading  # Usamos threading para ejecutar el juego de trivia en un hilo separado

# Crear el pool de conexiones al iniciar la aplicación
create_connection_pool()

app = FastAPI()

@app.get("/")
def read_root():
    # Llama a la función get_all_questions para obtener todas las preguntas
    questions = get_all_questions()
    # Devuelve las preguntas como respuesta
    return {"questions": questions}

@app.get("/start_quiz")
def start_quiz():
    """
    Inicia el juego de trivia.
    """
    # Ejecutar el juego de trivia en un hilo separado
    threading.Thread(target=run_quiz).start()
    return {"message": "El juego de trivia ha comenzado. Revisa la consola para jugar."}