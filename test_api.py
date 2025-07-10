import requests

def test_predict():
    url = "http://127.0.0.1:8000/predict"
    payload = {"text": "I love coding in Python and JavaScript."}
    response = requests.post(url, json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "tags" in data
    assert isinstance(data["tags"], list)
