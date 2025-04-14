import pytest
from app.trivia import Quiz

def test_quiz_scoring():
    """
    Testea la función answer_question de la clase Quiz.
    Se asegura de que el puntaje se actualice correctamente al responder preguntas.
    """
    # Creamos un cuestionario de ejemplo
    quiz = Quiz()
    question1 = Question("¿Cuál es la capital de Francia?", ["Madrid", "Londres", "París", "Berlín"], 3)
    quiz.add_question(question1)
    assert quiz.answer_question(3) == True  # Respuesta correcta
    assert quiz.get_score() == 1  # Puntaje debe ser 1
    assert quiz.answer_question(1) == False  # Respuesta incorrecta
    assert quiz.get_score() == 1  # Puntaje sigue siendo 1

def test_quiz_reset():
    """
    Testea la función reset_quiz de la clase Quiz.
    Se asegura de que el cuestionario se reinicie correctamente.
    """
    # Creamos un cuestionario de ejemplo
    quiz = Quiz()
    question1 = Question("¿Cuál es la capital de Francia?", ["Madrid", "Londres", "París", "Berlín"], 3)
    quiz.add_question(question1)
    quiz.answer_question(3)  # Respuesta correcta
    assert quiz.get_score() == 1  # Puntaje debe ser 1
    quiz.reset_quiz()  # Reiniciamos el cuestionario
    assert quiz.get_score() == 0  # Puntaje debe ser 0 después del reinicio

def test_quiz_get_score():
    """
    Testea la función get_score de la clase Quiz.
    Se asegura de que el puntaje se calcule correctamente.
    """
    quiz = Quiz()
    question1 = Question("¿Cuál es la capital de Francia?", ["Madrid", "Londres", "París", "Berlín"], 3)
    quiz.add_question(question1)
    quiz.answer_question(3)  # Respuesta correcta
    assert quiz.get_score() == 1  # Puntaje debe ser 1

def test_quiz_answer_question():
    """
    Testea la función answer de la clase Quiz.
    Se asegura de que el puntaje se actualice correctamente al responder preguntas.
    """
    quiz = Quiz()
    question1 = Question("¿Cuál es la capital de Francia?", ["Madrid", "Londres", "París", "Berlín"], 3)
    quiz.add_question(question1)
    assert quiz.answer_question(3) == True  # Respuesta correcta
    assert quiz.get_score() == 1  # Puntaje debe ser 1
    assert quiz.answer_question(1) == False  # Respuesta incorrecta
    assert quiz.get_score() == 1  # Puntaje sigue siendo 1

def test_quiz_get_next_question():
    """
    Testea la función get_next_question de la clase Quiz.
    Se asegura de que se devuelva la siguiente pregunta correctamente.
    """
    quiz = Quiz()
    question1 = Question("¿Cuál es la capital de Francia?", ["Madrid", "Londres", "París", "Berlín"], 3)
    question2 = Question("¿Cuál es la capital de España?", ["Madrid", "Londres", "París", "Berlín"], 1)
    quiz.add_question(question1)
    quiz.add_question(question2)
    assert quiz.get_next_question() == question1  # Debe devolver la primera pregunta
    assert quiz.get_next_question() == question2  # Debe devolver la segunda pregunta
    assert quiz.get_next_question() == None  # No hay más preguntas, debe devolver None


def test_quiz_delete_question():
    """
    Testea la función delete_question de la clase Quiz.
    Se asegura de que una pregunta se elimine correctamente del cuestionario.
    """
    quiz = Quiz()
    question1=Question("¿Cuál es la capital de Francia?", ["Madrid", "Londres", "París", "Berlín"], 3)
    question2=Question("¿Cuál es la capital de España?", ["Madrid", "Londres", "París", "Berlín"], 1)
    quiz.add_question(question1)
    quiz.add_question(question2)
    quiz.delete_question(question1)  # Eliminamos la primera pregunta
    assert quiz.get_next_question() == question2  # Debe devolver la segunda pregunta
    assert quiz.get_next_question() == None  # No hay más preguntas, debe devolver None

