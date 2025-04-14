from app.trivia import Question  
from app.db.db_connection import get_connection_from_pool, release_connection_to_pool

def get_questions_by_difficulty(difficulty):
    """
    Obtiene las preguntas de la base de datos filtradas por dificultad.
    :param difficulty: La dificultad de las preguntas que se desean obtener.
    :return: Lista de preguntas.
    """
    conn = get_connection_from_pool()
    if not conn:
        print("Error: No se pudo obtener una conexión del pool.")
        return []

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM trivia.questions WHERE difficulty = %s", (difficulty,))
        rows = cursor.fetchall()
        # print(f"Preguntas obtenidas: {len(rows)}")

        # Convertimos las filas en objetos de tipo Question
        questions = []
        for row in rows:
            question_text = row[1]
            options = row[2:6]
            correct_answer = row[6]
            difficulty = row[7]
            questions.append(Question(question_text, options, correct_answer, difficulty))

        cursor.close()
        return questions
    except Exception as e:
        print(f"Error al obtener las preguntas: {e}")
        return []
    finally:
        release_connection_to_pool(conn)
