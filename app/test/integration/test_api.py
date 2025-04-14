from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_questions_by_difficulty():
    """
    Testea el endpoint /questions/{difficulty} para obtener preguntas de trivia.
    """
    # Test para dificultad fácil
    response = client.get("/questions/fácil")
    assert response.status_code == 200
    data = response.json()
    assert "questions" in data
    assert len(data["questions"]) > 0

    #Test para dificultad media
    response = client.get("/questions/media")
    assert response.status_code == 200
    data = response.json()
    assert "questions" in data
    assert len(data["questions"]) > 0

    #Test para dificultad difícil
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