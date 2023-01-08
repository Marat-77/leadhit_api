from config.db import connect_mongo
from models.form_templates import insert_one_data

# добавление документов в БД

if __name__ == '__main__':
    data1 = {"name": "User Form template",
             "user_email": "email",
             "user_phone": "phone",
             "user_birthdate": "date",
             "user_name": "text"}
    data2 = {"name": "Address Form template",
             'address_city': 'text',
             "address_street": "text"}
    list_examples = [data1, data2]
    coll = connect_mongo()

    # count_docs = coll.count_documents({})
    # print(count_docs)
    # coll.drop()
    # count_docs = coll.count_documents({})
    # print(count_docs)

    results = []
    for d in list_examples:
        res = coll.find_one(d)
        if not res:
            res_id = insert_one_data(coll, d)
            results.append(str(res_id))
    if results:
        print(f'добавлены документы. id: {", ".join(results)}')
    count_docs = coll.count_documents({})
    print(f'В коллекции "{coll.name}" документов: {count_docs}')
