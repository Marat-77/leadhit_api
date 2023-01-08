import requests
from requests.exceptions import RequestException

# http://127.0.0.1:8000/data/?field1=asd@sdf.ru&field2=+79011234567&field3=2022-12-31&field4=dsdfsd123ssdf33
url = 'http://127.0.0.1:8000/'

path = 'get_form/'

# =====================================================
d1 = {'user_email': 'email@mail.ru',
      'user_phone': '+79011234567',
      'user_birthdate': '2022-11-11',
      'user_name': 'Alex'}

d2 = {'user_email': 'email@mail.ru',
      'user_phone': '+7 901 123 45 67',
      'user_birthdate': '1945-05-09',
      'user_name': 'Boris'}

d3 = {'user_email': 'ema-12il@mail.com',
      'user_phone': '+7-901-123-45-67',
      'user_birthdate': '08.01.2023',
      'last_name': 'Bar',
      'user_name': 'Foo'}

d4 = {'user_email': 'em@a-12il@mail.com',
      'user_phone': '+7-101-123-45-67',
      'user_birthdate': '30.02.2022',
      'last_name': 'text'}

d5 = {'user_email': 'email@mail.ru',
      'user_phone': '+7 901 123 45 67',
      'user_birthdate': '1945-05-09',
      'user_name': 'Егор'}

params_list = [d1, d2, d3, d4, d5]
# =====================================================

# with session
with requests.session() as session:
    for params in params_list:
        try:
            response = session.post(url + path, params=params, timeout=5)
            if response.ok:
                print('параметры запроса:', params)
                print('статус код:', response.status_code)
                print('json ответ:', response.json())
                print('тип данных ответа:', response.headers['content-type'])
                print('-' * 15)
            else:
                print(response.status_code)
        except RequestException as err:
            print(err)
