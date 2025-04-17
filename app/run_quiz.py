from app.db.db_queries import get_questions_by_difficulty
from app.trivia import Quiz


def run_menu():
    print("\n=======================================")
    print("¡Bienvenido al juego de trivia!")
    print("=======================================")

    option = 0
    difficulty = "fácil" # Por defecto, la dificultad es fácil
    
    while option != 1: 

        print("\n1. Iniciar juego") 
        print("2. Seleccionar dificultad")
        print("3. Salir")

        option = int(input("Selecciona una opción (1-3): "))
  
        if option == 1:
            print("Iniciando juego...")
            print("Dificultad actual:", difficulty)
            run_quiz(difficulty)

        elif option == 2:
            print("\nSeleccionando dificultad...")
            print("1. Fácil")
            print("2. Medio")
            print("3. Difícil")
            option = int(input("Selecciona una opción (1-3): "))
            if option == 1:
                difficulty = "fácil"
            elif option == 2:
                difficulty = "media"
            elif option == 3:
                difficulty = "difícil"
            else:
                print("Opción no válida")
                return

        elif option == 3:
            print("Saliendo del juego...")
            return 
        else:
            print("Opción no válida")
        
def run_quiz(difficulty: str, number_of_questions: int = 10):
    # Obtener preguntas de la base de datos
    questions_data = get_questions_by_difficulty(difficulty)
    
    # Si no se obtienen suficientes preguntas, mostramos un mensaje
    if len(questions_data) < number_of_questions:
        print("No hay suficientes preguntas en la base de datos.")
        return
    
    # Crear el cuestionario con las preguntas obtenidas
    quiz = Quiz(questions_data[:number_of_questions])  # Limitar al número deseado de preguntass
    
    # Empezar el juego
    while True:
        question = quiz.get_next_question()
        if question:
            print(f"\nPregunta: {question.get_question_text()}")
            print("Opciones:")
            # Mostrar opciones de respuesta
            for i, option in enumerate(question.get_options(), start=1):
                print(f"{i}. {option}")
            print(f"Tu puntaje actual es: {quiz.get_score()}/{number_of_questions}")
            answer = int(input("Selecciona una opción (1-4): "))
            # Validar la respuesta
            try:
                if quiz.answer_question(answer):
                    print("\n¡Correcto!")
                else:
                    print("\nIncorrecto.")
            except ValueError as e:
                print(e)
        else:
            print("\n=======================================")
            print("No hay más preguntas.")
            print("Juego terminado.")
            print("=======================================")
            break

    print(f"Tu puntaje final es: {quiz.get_score()}/{quiz.get_total_questions()}")