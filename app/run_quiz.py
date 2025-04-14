from app.db.db_queries import get_all_questions
from app.trivia import Quiz


def run_quiz(number_of_questions=10):
    print("Bienvenido al juego de trivia!")
    print("Responde las siguientes preguntas:")
    
    # Obtener preguntas de la base de datos
    questions_data = get_all_questions()
    
    # Si no se obtienen suficientes preguntas, mostramos un mensaje
    if len(questions_data) < number_of_questions:
        print("No hay suficientes preguntas en la base de datos.")
        return
    
    # Crear el cuestionario con las preguntas obtenidas
    quiz = Quiz(questions_data[:number_of_questions])  # Limitar al número deseado de preguntas
    
    # Empezar el juego
    while True:
        question = quiz.get_next_question()
        if question:
            print(f"Pregunta: {question.get_question_text()}")
            print("Opciones:")
            # Mostrar opciones de respuesta
            for i, option in enumerate(question.get_options(), start=1):
                print(f"{i}. {option}")
            print("5. Mostrar puntaje")
            print(f"Tu puntaje actual es: {quiz.get_score()}/{quiz.current_question_index}")
            answer = int(input("Selecciona una opción (1-5): "))
            # Validar la respuesta
            
            
            try:
                if quiz.answer_question(answer):
                    print("¡Correcto!")
                else:
                    print("Incorrecto.")
            except ValueError as e:
                print(e)
        else:
            print("No hay más preguntas.")
            print("Juego terminado.")
            break

    print(f"Tu puntaje final es: {quiz.get_score()}/{quiz.get_total_questions()}")