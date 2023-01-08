from typing import List

import pymongo
from pymongo.errors import PyMongoError


def insert_one_data(coll: pymongo.collection.Collection,
                    data: dict):
    """
    Добавление документа в коллекцию БД Монго
    :param coll:
    :param data:
    :return: _id добавленного документа
    """
    try:
        result = coll.insert_one(data)
        return result.inserted_id
    except PyMongoError as err:
        print(err)


def insert_many_data(coll: pymongo.collection.Collection,
                     list_data: List[dict]):
    """
    Добавление документов в коллекцию БД Монго
    :param coll:
    :param list_data:
    :return: список _id добавленных документов
    """
    try:
        result = coll.insert_many(list_data)
        return result.inserted_ids
    except PyMongoError as err:
        print(err)


def find_all_templates(coll: pymongo.collection.Collection):
    """
    Ищем все шаблоны из коллекции шаблонов.
    :param coll:
    :return:
    """
    try:
        # res = coll.find()
        return coll.find()
    except PyMongoError as err:
        print(err)
