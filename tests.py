from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_calculate():
    response = client.post("/calculate/10/5/+")
    assert response.status_code == 200
    assert response.json()["task_id"] == 1


def test_get_result():
    response = client.get("/result/1")
    assert response.status_code == 200
    assert response.json()["status"] == "completed"
    assert response.json()["result"] == 15


def test_get_tasks():
    response = client.get("/tasks")
    assert response.status_code == 200
    assert response.json() == {"1": {"status": "completed", "result": 15}}


def test_invalid_operator():
    response = client.post("/calculate/10/5/invalid_operator")
    assert response.status_code == 400
    assert (
        response.json()["detail"]
        == "Invalid operator. Supported operators are +, -, *, \\"
    )


def test_invalid_task_id():
    response = client.get("/result/1000")  # Assuming task with ID 1000 does not exist
    assert response.status_code == 404
    assert response.json()["detail"] == "Task not found"


def test_invalid_input_type():
    response = client.post("/calculate/10.5/5/+")
    assert response.status_code == 422


def test_invalid_operator_type():
    response = client.post("/calculate/10/5/invalid_operator")
    assert response.status_code == 400


def test_invalid_task_id_type():
    response = client.get("/result/invalid_task_id")
    assert response.status_code == 422
