class Question:
    def __init__(self, description, options, correct_answer):
        """
        Inicializa la clase Question con los atributos necesarios.

        :param description: Descripción de la pregunta.
        :param options: Lista de opciones para la pregunta.
        :param correct_answer: El número de la opción correcta (1, 2, 3, 4).
        """
        self.description = description
        self.options = options
        self.correct_answer = correct_answer

    def is_correct(self, answer):
        """
        Verifica si la respuesta proporcionada es correcta.

        :param answer: Número de la opción seleccionada por el jugador (1, 2, 3, 4).
        :raises ValueError: Si la respuesta no es un número entero o está fuera del rango de opciones.
        :return: True si la respuesta es correcta, False si es incorrecta.
        """
                
        if not isinstance(answer, int):
            raise ValueError("La respuesta debe ser un número entero.")

        if answer < 1 or answer > len(self.options):
            raise ValueError("La respuesta debe estar entre el número de opciones disponibles.")
                
        return self.correct_answer == answer

class Quiz:
    def __init__(self,questions):
        """
        Inicializa la clase Quiz con una lista de preguntas.

        :param questions: Lista de objetos Question.
        """
        self.questions = questions
        self.current_question_index = 0
        self.score = 0
        self.total_questions = len(self.questions)
    
    def add_question(self, question):
        """
        Agrega una pregunta a la lista de preguntas del cuestionario.

        :param question: Objeto Question a agregar.
        """
        self.questions.append(question)
        self.total_questions += 1 
    
    def get_next_question(self):
        """
        Obtiene la siguiente pregunta del cuestionario.

        :return: La siguiente pregunta o None si no hay más preguntas.
        """
        if self.current_question_index < self.total_questions:
            question = self.questions[self.current_question_index]
            self.current_question_index += 1
            return question
        else:
            return None

    def answer_question(self, answer):
        """
        Responde a la pregunta actual y actualiza el puntaje.

        :param answer: Número de la opción seleccionada por el jugador (1, 2, 3, 4).
        :raises ValueError: Si la respuesta no es un número entero o está fuera del rango de opciones.
        :return: True si la respuesta es correcta, False si es incorrecta.
        """
        question = self.questions[self.current_question_index - 1]
        if question.is_correct(answer):
            self.score += 1
            return True
        else:
            return False

    def delete_question(self, question):
        """
        Elimina una pregunta del cuestionario.

        :param question: Objeto Question a eliminar.
        """
        self.questions.remove(question)
        self.total_questions -= 1
        self.current_question_index -= 1
        if self.current_question_index < 0:
            self.current_question_index = 0
        if self.total_questions == 0:
            self.current_question_index = 0
            self.score = 0

    def get_score(self):
        """
        Calcula el puntaje del jugador.

        :return: El puntaje total.
        """
        return self.score
           
    def reset_quiz(self):
        """
        Reinicia el cuestionario a su estado inicial.

        :return: None
        """
        self.current_question_index = 0
        self.score = 0


