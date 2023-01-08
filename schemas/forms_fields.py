from datetime import datetime
import re
from pydantic import BaseModel, EmailStr, validator, ValidationError


class EmailField(BaseModel):
    """
    Класс EmailField
    для валидации email-адреса
    """
    email: EmailStr


class PhoneNumber(BaseModel):
    """
    Класс PhoneNumber
    Валидация телефонного номера РФ:
    допустимые номера:
    +7xxxxxxxxxx
    +7 xxx xxx xx xx
    +7-xxx-xxx-xx-xx
    телефонные коды РФ.
    """
    phone_number: str

    @validator('phone_number')
    def ru_phone_validation(cls, v):
        regex = r'^(\+7)[\-\s]?([3489]\d{2})[\-\s]?(\d{3})[\-\s]?(\d{2})[\-\s]?(\d{2})$'
        re_comp = re.compile(regex)
        if v and not re.search(regex, v, re.I):
            raise ValueError('not Russian phone number')
        return ''.join(re_comp.search(v).groups())


def check_date(date_: str):
    """
    Валидируем дату.
    Допустимый формат:
    DD.MM.YYYY или YYYY-MM-DD
    :param date_:
    :return:
    """
    try:
        date_obj = datetime.strptime(date_, '%Y-%m-%d')
        # print(date_, date_obj)
        # print(type(date_obj))
        return True
    except ValueError:
        try:
            date_obj = datetime.strptime(date_, '%d.%m.%Y')
            # print(date_obj)
            # print(type(date_obj))
            return True
        except ValueError as err:
            # print(date_, err)
            return False


def check_phone(input_phone: str):
    try:
        ph = PhoneNumber(phone_number=input_phone)
        # print(input_phone, ph.json())
        return True
    except ValidationError as err:
        # print(err)
        # print(input_phone, err.json())
        return False


def check_email(input_email: str):
    """
    Валидируем email-адрес
    :param input_email:
    :return:
    """
    try:
        user2 = EmailField(email=input_email)
        # user2.dict()
        # user2.json()
        return True
    except ValidationError as err:
        # print(err)
        return False


def check_data(value):
    """
    Валидируем данные и присваиваем соответсвующее имя типа.
    :param value:
    :return:
    """
    if not value:
        return None
    if check_date(str(value)):
        return 'date'
    elif check_phone(str(value)):
        return 'phone'
    elif check_email(str(value)):
        return 'email'
    else:
        return 'text'
