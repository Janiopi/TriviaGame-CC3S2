import pytest
from trivia import Question, Quiz


def test_question_correct_answer():
    """
    Testea la función is_correct de la clase Question.
    Se asegura de que la respuesta correcta devuelva True.
    """
    # Creamos una pregunta de ejemplo
    question = Question("¿Cuál es la capital de Francia?", ["Madrid", "Londres", "París", "Berlín"], 3)
    
    # Comprobamos que la respuesta correcta es la opción 3 (París)
    assert question.is_correct(3) == True

def test_question_incorrect_answer():
    """
    Testea la función is_correct de la clase Question.
    Se asegura de que la respuesta incorrecta devuelva False.
    """
    # Creamos una pregunta de ejemplo
    question = Question("¿Cuál es la capital de Francia?", ["Madrid", "Londres", "París", "Berlín"], 3)
    
    # Comprobamos que la respuesta incorrecta no es correcta
    assert question.is_correct(1) == False

def test_question_non_integer_answer():
    """
    Testea la función is_correct de la clase Question.
    Se asegura de que se lance una excepción si la respuesta no es un número entero.
    """
    # Creamos una pregunta de ejemplo
    question = Question("¿Cuál es la capital de Francia?", ["Madrid", "Londres", "París", "Berlín"], 3)
    
    # Comprobamos que se lanza una excepción si la respuesta no es un número entero
    with pytest.raises(ValueError,match="La respuesta debe ser un número entero."):
        question.is_correct("Paris") #Debe lanzar una exceptcion

def test_question_out_of_range_answer():
    """
    Testea la función is_correct de la clase Question.
    Se asegura de que se lance una excepción si la respuesta está fuera del rango de opciones.
    """
    #Creamos una pregunta de ejemplo
    question = Question("¿Cuál es la capital de Francia?", ["Madrid", "Londres", "París", "Berlín"], 3)
    
    # Comprobamos que se lanza una excepción si la respuesta está fuera del rango de opciones
    with pytest.raises(ValueError,match="La respuesta debe estar entre el número de opciones disponibles."):
        question.is_correct(5) #Debe lanzar una exceptcion


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

