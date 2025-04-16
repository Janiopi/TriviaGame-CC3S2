import unittest
from app.trivia import Question

class TestQuestion(unittest.TestCase):
    
    def test_question_correct_answer(self):
        """
        Testea la función is_correct de la clase Question.
        Se asegura de que la respuesta correcta devuelva True.
        """
        question = Question("¿Cuál es la capital de Francia?", ["Madrid", "Londres", "París", "Berlín"], 3)
        self.assertTrue(question.is_correct(3))  

    def test_question_incorrect_answer(self):
        """
        Testea la función is_correct de la clase Question.
        Se asegura de que la respuesta incorrecta devuelva False.
        """
        question = Question("¿Cuál es la capital de Francia?", ["Madrid", "Londres", "París", "Berlín"], 3)
        self.assertFalse(question.is_correct(1))  

    def test_question_non_integer_answer(self):
        """
        Testea la función is_correct de la clase Question.
        Se asegura de que se lance una excepción si la respuesta no es un número entero.
        """
        question = Question("¿Cuál es la capital de Francia?", ["Madrid", "Londres", "París", "Berlín"], 3)
        with self.assertRaises(ValueError):  
            question.is_correct("Paris")

    def test_question_out_of_range_answer(self):
        """
        Testea la función is_correct de la clase Question.
        Se asegura de que se lance una excepción si la respuesta está fuera del rango de opciones.
        """
        question = Question("¿Cuál es la capital de Francia?", ["Madrid", "Londres", "París", "Berlín"], 3)
        with self.assertRaises(ValueError):
            question.is_correct(5)
