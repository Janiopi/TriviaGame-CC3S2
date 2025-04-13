from fastapi import FastAPI
from app.db.db_connection import create_connection_pool
from app.db.db_queries import get_all_questions
from app.run_quiz import run_quiz

# Crear el pool de conexiones al iniciar la aplicación
create_connection_pool()

app = FastAPI()

@app.get("/")
def read_root():
    #Llama la función get_all_questions para obtener todas las preguntas
    questions = get_all_questions()
    # Devuelve las preguntas como respuesta
    return {"questions": questions}

@app.get("/start_quiz")
def start_quiz():
    # Ejecutar el quiz
    run_quiz()
    return {"message": "El quiz ha comenzado, pero necesitas tener acceso a la consola para interactuar."}
