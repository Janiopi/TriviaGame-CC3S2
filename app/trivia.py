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


