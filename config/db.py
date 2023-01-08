from pymongo import MongoClient
from pymongo.errors import PyMongoError

from config.settings import DB_HOST, DB_PORT, DB_TIMEOUT


def connect_mongo():
    client = MongoClient(DB_HOST,
                         DB_PORT,
                         serverSelectionTimeoutMS=DB_TIMEOUT)
    try:
        client.server_info()
        db = client['my_db']
        form_collection = db['form_templates']
        return form_collection
    except PyMongoError as err:
        print(err)
