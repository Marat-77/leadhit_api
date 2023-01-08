# from bson import ObjectId
from fastapi import APIRouter, Request

from config.settings import SERVER_LOGGER
from services.search_form_templates import search_form_templates

form_tmp = APIRouter()


@form_tmp.get('/')
async def index():
    return {"message": "Hello world!"}


@form_tmp.post('/get_form/')
async def api_get_form_post(request: Request):
    """
    Обрабатываем post-запрос.
    Получаем параметры запроса.
    Возвращаем имя соответствующего шаблона в виде
    {"name": "имя соответствующего шаблона"}
    пример:{'name': 'User Form template'}
    {
      "name":"User Form template"
    }
    или (если нет соответствий)
    {
      "имя параметра": "тип",
      "имя параметра": "тип"
    }
    пример:
    {
      "field1":"email",
      "field2":"text",
      "field3":"date",
      "field4":"text"
    }
    :param request:
    :return:
    """
    params = request.query_params
    result = search_form_templates(params)
    SERVER_LOGGER.debug(f'params: {str(params)}, result: {str(result)}')
    return result


# http://127.0.0.1:8000/get_form/?user_email=email%40mail.ru&user_phone=%2B7+901+123+45+67&user_birthdate=08.01.2023&user_name=Boris
@form_tmp.get('/get_form/')
async def api_get_form_get(request: Request):
    params = request.query_params
    result = search_form_templates(params)
    return result
# TODO почистить код и добавить логирование
