from typing import List, Union, Dict

import pymongo
from starlette.datastructures import QueryParams

from config.db import connect_mongo
from config.settings import SERVER_LOGGER
from models.form_templates import find_all_templates
from schemas.forms_fields import check_data


def parse_query_params(params: QueryParams) -> dict:
    """
    Преобразуем параметры запроса в словарь с типами.
    :param params:
    :return:
    """
    # result = {k: check_data(v) for k, v in params.items()}
    return {k: check_data(v) for k, v in params.items()}


def serialize_dict(from_mongo: dict) -> dict:
    """
    Сериализуем словарь (документ из БД MongoDB) в словарь (шаблонов)
    без _id.
    :param from_mongo:
    :return:
    """
    # dict_template = {i: from_mongo[i] for i in from_mongo if i != '_id'}
    # dict_id = {i: str(from_mongo[i]) for i in from_mongo if i == '_id'}
    # dict_with_id = {**dict_id, **dict_template}
    return {k: from_mongo[k] for k in from_mongo if k != '_id'}


def serialize_list(from_mongo: pymongo.cursor.Cursor) -> List[dict]:
    """
    Сериализуем данные полученные из БД MongoDB (тип курсор MongoDB)
    в список словарей (шаблонов).
    :param from_mongo:
    :return: Список словарей (шаблонов).
    """
    return [serialize_dict(a) for a in from_mongo]


def templates_set(teplates: List[dict]) -> List[List[set]]:
    """
    Из списка словарей создаем списки списков
     ['имя шаблона', <множество кортежей (ключ, значение)>]
    :param teplates:
    :return:
    """
    return [[d['name'], {(k, v) for k, v in d.items() if k != 'name'}] for d in teplates]


def check_form(check_dict: dict, templs: List[List[Union[str, set]]]):
    """
    Ищем совпадение шаблона.
    Возвращаем имя соответствующего шаблона или словарь параметров запроса с типами.
    :param check_dict: Словарь параметров запроса с типами.
    :param templs: Списки ['имя шаблона', <множество кортежей (ключ, значение)>]
    :return:
    """
    # создаем множество (ключ, значение) из словаря параметров запроса:
    check_set = {item for item in check_dict.items()}
    for t in templs:
        if t[1].issubset(check_set):
            return {'name': t[0]}
        else:
            return check_dict


def search_form_templates(params: QueryParams) -> Dict[str, str]:
    """
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
    :param params:
    :return:
    """
    # получаем словарь из параметров запроса:
    dict_from_params = parse_query_params(params)
    # подключаемся к MongoDB:
    templates_collection = connect_mongo()
    # получаем все шаблоны из коллекции (тип курсор):
    tmps_from_mongo = find_all_templates(templates_collection)
    # сериализуем полученные из БД шаблоны в список словарей:
    lst_from_mongo = serialize_list(tmps_from_mongo)
    # print('38res:', res)
    # получаем списки списков множеств:
    list_templates_set = templates_set(lst_from_mongo)
    # print('list_templates_set:', list_templates_set)
    # получаем результат сравнения шаблонов из БД и запроса:
    my_res = check_form(dict_from_params, list_templates_set)
    # print(f'{my_res=}')
    SERVER_LOGGER.debug(f'params: {str(params)}, result: {str(my_res)}')
    return my_res
