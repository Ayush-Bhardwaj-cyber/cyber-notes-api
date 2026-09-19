from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200

def test_get_notes():
    client = app.test_client()
    response = client.get("/notes")
    assert response.status_code == 200

def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200

def test_add_note():
    client = app.test_client()

    response = client.post(
        "/notes",
        json={
            "title": "Nmap",
            "content": "Network scanning tool"
        }
    )

    assert response.status_code == 201