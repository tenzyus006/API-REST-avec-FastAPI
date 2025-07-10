import requests

def test_predict():
    url = "https://apifastheroku-8bd7a41e1bb2.herokuapp.com/predict"  # or your deployed API URL
    payload = {"text": "I love coding in Python and JavaScript."}
    response = requests.post(url, json=payload)
    assert response.status_code == 200, f"Status code was {response.status_code}"
    data = response.json()
    assert "tags" in data, "'tags' not in response"
    assert isinstance(data["tags"], list), "'tags' is not a list"

if __name__ == "__main__":
    test_predict()
    

