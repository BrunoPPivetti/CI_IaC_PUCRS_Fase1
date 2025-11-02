from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_status():
    response = client.get('/status')
    assert response.status_code == 200
    assert response.json() == {'status':'OK'}

def test_hello():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'Hello':'World'}