
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
        cursor.execute("SELECT question_id, question_text, option_1, option_2, option_3, option_4, correct_answer FROM trivia.questions")
        rows = cursor.fetchall()
        
        # Convertir las filas en objetos de tipo Question
        questions = []
        for row in rows:
            question_id, question_text, option_1, option_2, option_3, option_4, correct_answer = row
            options = [option_1, option_2, option_3, option_4]
            questions.append({
                "id": question_id,
                "question_text": question_text,
                "options": options,
                "correct_answer": correct_answer
            })
        
        cursor.close()
        return questions
    except Exception as e:
        print(f"Error al obtener las preguntas: {e}")
        return []
    finally:
        release_connection_to_pool(conn)


