from fastapi.testclient import TestClient
from app.main import app
from unittest import mock

# Inicializa el cliente de pruebas
client = TestClient(app)

# Creamos un conjunto de datos simulado
mock_questions = [
    {"question_id": 1, "question_text": "¿Cuál es la capital de Francia?", "option_1": "Madrid", "option_2": "Londres", "option_3": "París", "option_4": "Berlín", "correct_answer": 3, "difficulty": "fácil"},
    {"question_id": 2, "question_text": "¿Quién pintó la Mona Lisa?", "option_1": "Da Vinci", "option_2": "Van Gogh", "option_3": "Picasso", "option_4": "Rembrandt", "correct_answer": 1, "difficulty": "fácil"},
    {"question_id": 3, "question_text": "¿Qué gas es el más abundante en la atmósfera?", "option_1": "Oxígeno", "option_2": "Nitrógeno", "option_3": "Carbono", "option_4": "Hidrógeno", "correct_answer": 2, "difficulty": "media"},
    {"question_id": 4, "question_text": "¿Qué país tiene la mayor población del mundo?", "option_1": "India", "option_2": "Estados Unidos", "option_3": "China", "option_4": "Indonesia", "correct_answer": 3, "difficulty": "media"},
    {"question_id": 5, "question_text": "¿Cuál es la capital de Japón?", "option_1": "Kyoto", "option_2": "Seúl", "option_3": "Pekín", "option_4": "Tokio", "correct_answer": 4, "difficulty": "difícil"},
    {"question_id": 6, "question_text": "¿En qué año comenzó la Segunda Guerra Mundial?", "option_1": "1935", "option_2": "1939", "option_3": "1941", "option_4": "1945", "correct_answer": 2, "difficulty": "difícil"}
]

@mock.patch('app.db.db_connection.get_questions_by_difficulty', return_value=mock_questions)

def test_get_questions_by_difficulty(mock_get_questions_by_difficulty):
    """
    #Testea el endpoint /questions/{difficulty} para obtener preguntas de trivia.
    """
    # Test para dificultad fácil
    response = client.get("/questions/fácil")
    assert response.status_code == 200
    data = response.json()
    assert "questions" in data
    assert len(data["questions"]) > 0

    # Test para dificultad media
    response = client.get("/questions/media")
    assert response.status_code == 200
    data = response.json()
    assert "questions" in data
    assert len(data["questions"]) > 0

    # Test para dificultad difícil
    response = client.get("/questions/difícil")
    assert response.status_code == 200
    data = response.json()
    assert "questions" in data
    assert len(data["questions"]) > 0

def test_root_endpoint():
    """
    Testea el endpoint raíz ("/") de la API.
    """
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert data["message"] == "Bienvenido a la API de Trivia!"
