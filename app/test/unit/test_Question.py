import pytest
from app.trivia import Question 


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

