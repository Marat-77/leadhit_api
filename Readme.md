# Web-приложение для определения заполненных форм.


---
### Для работы необходимо:

1. Установить fastapi и другие необходимые пакеты:
```commandline
pip install fastapi
pip install pymongo
pip install uvicorn

# для валидации email:
pip install pydantic[email]
# или
pip install email-validator

# для тестов:
pip install pytest
pip install httpx
pip install requests
```
или
```commandline
pip install -r requirements.txt
# или
python -m pip install -r requirements.txt
```
2. Запустить контейнер с MongoDB:
```commandline
sudo docker run --rm -d --name mongo_fa -p 27017:27017 -v mongodb_fa:/data/db -v mongodb_fa_config:/data/configdb mongo
```

Настройки хранятся в `/config/settings.py` и `/config/db.py`

Файл логов: `/logs/server.log`
(время в UTC)

3. Перед первым запуском необходимо заполнить БД тестовыми данными:
   - запустите `run_first.py`

4. запустите: `uvicorn main:app --reload`

5. Для тестов:
   - основной тест: `/leadhit_api$ pytest -v test_main.py`
   - протестировать с помощью *requests*: запустите `try_request.py`
   - тесты некоторых функций: `/leadhit_api$ python -m pytest -v tests/test_functions.py`