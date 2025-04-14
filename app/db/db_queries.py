from app.trivia import Question  
from app.db.db_connection import get_connection_from_pool, release_connection_to_pool

def get_all_questions():
    """
    Obtiene todas las preguntas de la base de datos.
    """
    conn = get_connection_from_pool()
    if not conn:
        print("Error: No se pudo obtener una conexión del pool.")
        return []

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT question_text, option_1, option_2, option_3, option_4, correct_answer FROM trivia.questions")
        rows = cursor.fetchall()

        # Convertimos las filas en objetos de tipo Question
        questions = []
        for row in rows:
            question_text = row[0]  # El texto de la pregunta (columna 0)
            options = row[1:5]  # Las opciones (columnas 1 a 4)
            correct_answer = row[5]  # La respuesta correcta (columna 5)
            questions.append(Question(question_text, options, correct_answer))
        
        cursor.close()
        return questions
    except Exception as e:
        print(f"Error al obtener las preguntas: {e}")
        return []
    finally:
        release_connection_to_pool(conn)
