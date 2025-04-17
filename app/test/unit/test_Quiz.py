import unittest
from app.trivia import Quiz, Question

class TestQuiz(unittest.TestCase):

    def test_quiz_scoring(self):
        """
        Testea la función answer_question de la clase Quiz.
        Se asegura de que el puntaje se actualice correctamente al responder preguntas.
        """
        question1 = Question("¿Cuál es la capital de Francia?", ["Madrid", "Londres", "París", "Berlín"], 3, "fácil")
        quiz = Quiz(questions=[question1])

        self.assertTrue(quiz.answer_question(3))  # Respuesta correcta
        self.assertEqual(quiz.get_score(), 1)  # Puntaje debe ser 1
        self.assertFalse(quiz.answer_question(1))  # Respuesta incorrecta
        self.assertEqual(quiz.get_score(), 1)  # Puntaje sigue siendo 1

    def test_quiz_reset(self):
        """
        Testea la función reset_quiz de la clase Quiz.
        Se asegura de que el cuestionario se reinicie correctamente.
        """
        question1 = Question("¿Cuál es la capital de Francia?", ["Madrid", "Londres", "París", "Berlín"], 3, "fácil")
        quiz = Quiz(questions=[question1])
        quiz.answer_question(3)  # Respuesta correcta

        self.assertEqual(quiz.get_score(), 1)  # Puntaje debe ser 1
        quiz.reset_quiz()  # Reiniciamos el cuestionario
        self.assertEqual(quiz.get_score(), 0)  # Puntaje debe ser 0 después del reinicio

    def test_quiz_get_score(self):
        """
        Testea la función get_score de la clase Quiz.
        Se asegura de que el puntaje se calcule correctamente.
        """
        question1 = Question("¿Cuál es la capital de Francia?", ["Madrid", "Londres", "París", "Berlín"], 3, "fácil")
        quiz = Quiz(questions=[question1])
        quiz.answer_question(3)  # Respuesta correcta

        self.assertEqual(quiz.get_score(), 1)  # Puntaje debe ser 1

    def test_quiz_get_next_question(self):
        """
        Testea la función get_next_question de la clase Quiz.
        Se asegura de que se devuelva la siguiente pregunta correctamente.
        """
        question1 = Question("¿Cuál es la capital de Francia?", ["Madrid", "Londres", "París", "Berlín"], 3, "fácil")
        question2 = Question("¿Cuál es la capital de España?", ["Madrid", "Londres", "París", "Berlín"], 1, "fácil")
        quiz = Quiz(questions=[question1, question2])

        self.assertEqual(quiz.get_next_question(), question1)  # Debe devolver la primera pregunta
        self.assertEqual(quiz.get_next_question(), question2)  # Debe devolver la segunda pregunta
        self.assertEqual(quiz.get_next_question(), None)  # No hay más preguntas, debe devolver None

    def test_quiz_delete_question(self):
        """
        Testea la función delete_question de la clase Quiz.
        Se asegura de que una pregunta se elimine correctamente del cuestionario.
        """
        question1 = Question("¿Cuál es la capital de Francia?", ["Madrid", "Londres", "París", "Berlín"], 3, "fácil")
        question2 = Question("¿Cuál es la capital de España?", ["Madrid", "Londres", "París", "Berlín"], 1, "fácil")
        quiz = Quiz(questions=[question1, question2])
        quiz.delete_question(question1)  # Eliminamos la primera pregunta

        self.assertEqual(quiz.get_next_question(), question2)  # Debe devolver la segunda pregunta
        self.assertEqual(quiz.get_next_question(), None)  # No hay más preguntas, debe devolver None
