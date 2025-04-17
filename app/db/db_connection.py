import psycopg2
import os
from dotenv import load_dotenv
from app.trivia import Question

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Conexión a la base de datos
def get_connection():
    """
    Establece la conexión con la base de datos PostgreSQL.
    """
    try:
        return psycopg2.connect(
            dbname=os.getenv("DB_NAME", "trivia_db"),
            user=os.getenv("DB_USER", "trivia_user"),
            password=os.getenv("DB_PASSWORD", "trivia_pass"),
            host=os.getenv("DB_HOST", "localhost"),
            port=os.getenv("DB_PORT", "5432")
        )
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def get_questions_by_difficulty(difficulty: str):
    """
    Obtiene las preguntas de la base de datos filtradas por dificultad.
    :param difficulty: La dificultad de las preguntas a obtener.
    :return: Lista de objetos de tipo Question.
    """
    conn = get_connection()
    if not conn:
        print("Error: No se pudo obtener la conexión a la base de datos.")
        return []

    questions = []
    try:
        with conn.cursor() as cursor:
            # Ejecutar la consulta
            cursor.execute(
                "SELECT question_text, option_1, option_2, option_3, option_4, correct_answer, difficulty "
                "FROM trivia.questions WHERE difficulty = %s", 
                (difficulty,)
            )
            rows = cursor.fetchall()

            # Convertir las filas en objetos de tipo Question
            for row in rows:
                question_text = row[0]
                options = row[1:5]
                correct_answer = row[5]
                difficulty = row[6]
                questions.append(Question(question_text, options, correct_answer, difficulty))

    except Exception as e:
        print(f"Error al ejecutar la consulta: {e}")
    finally:
        conn.close()  # Asegurarse de cerrar la conexión

    return questions
