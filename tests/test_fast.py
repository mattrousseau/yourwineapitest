from fastapi.testclient import TestClient
import pytest
from main import app
import json

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello stranger! This API allow you to evaluate the quality of red wine. Go to the /docs for more details."}

def test_predict():
    response = client.post(
        "/predict",
        headers={'accept': 'application/json', 'Content-Type': 'application/json'},
        json={'alcohol':9.4, 'volatile_acidity': 0.7},
    )
    assert response.status_code == 200
    result = json.loads(response.json())

    assert set(result) == {"prediction", "probability"}
    assert result["prediction"] == 0
    assert result["probability"] == pytest.approx(
        [0.7759315070304591, 0.22406849296954087],
        rel=0,
        abs=1e-12,
)

