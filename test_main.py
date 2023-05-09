from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_file():
    response = client.post(
        "/uploadfile/",
        files={"file": ("test_file.pdf", b"Hello World")}
    )
    assert response.status_code == 200
    assert response.json() == {"test_file.pdf" : "Hello World"}