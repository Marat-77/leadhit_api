from fastapi.testclient import TestClient

from routers.forms_tmp import form_tmp

client = TestClient(form_tmp)


def test_get_form_good():
    response = client.post('/get_form/?user_email=email%40mail.ru&user_phone=%2B7+901+123+45+67&user_birthdate=1945-05-09&user_name=Boris')
    assert response.status_code == 200
    assert response.json() == {"name": "User Form template"}


def test_get_form_none():
    response = client.post('/get_form/?user_email=em%40a-12il%40mail.com&user_phone=%2B7-101-123-45-67&user_birthdate=30.02.2022&last_name=text')
    assert response.status_code == 200
    assert response.json() == {"user_email": "text", "user_phone": "text", "user_birthdate": "text", "last_name": "text"}

# /leadhit_api$ pytest -v test_main.py
