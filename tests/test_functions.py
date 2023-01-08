import pytest
from schemas.forms_fields import check_data
from services.search_form_templates import check_form
# /leadhit_api$ python -m pytest -v tests/test_functions.py

list_examples = [('Foo', 'text'),
                 ('my@mail.ru', 'email'),
                 ('my@mail.ccom', 'email'),
                 ('m@y@mail.ru', 'text'),
                 ('+79011234567', 'phone'),
                 ('+7 901 123 45 67', 'phone'),
                 ('+7-901-123-45-67', 'phone'),
                 ('+7-901-123-45-671', 'text'),
                 ('+7-101-123-45-67', 'text'),
                 ('2022-12-31', 'date'),
                 ('31.12.2022', 'date'),
                 ('38.12.2022', 'text'),
                 ('123 it is text', 'text'),
                 ('+7-101-123-45-67', 'text'),
                 (5, 'text'),
                 ('', None)]


@pytest.mark.parametrize('value, expected_result', list_examples)
def test_check_data(value, expected_result):
    assert check_data(value) == expected_result


d_test1 = {'par1': 'text',
           'par2': 'text',
           'my': 'text',
           'param5': 'date',
           'param6': 'date'}
d_test2 = {'user_email': 'email',
           'user_name': 'text',
           'user_phone': 'phone',
           'user_birthdate': 'date'}
d_test3 = {'user_email': 'email',
           'user_name': 'text',
           'user_phone': 'phone',
           'user_birthdate': 'date',
           'param6': 'date'}

tmps_set = [['User Form template',
             {('user_email', 'email'),
              ('user_name', 'text'),
              ('user_phone', 'phone'),
              ('user_birthdate', 'date')}],
            ['Address Form template',
             {('address_street', 'text'), ('address_city', 'text')}]]

lst_examples2 = [(d_test1, tmps_set, d_test1),
                  (d_test2, tmps_set, {'name': 'User Form template'}),
                  (d_test3, tmps_set, {'name': 'User Form template'})]


@pytest.mark.parametrize('test_dict, test_lst, expected_result', lst_examples2)
def test_check_form(test_dict, test_lst, expected_result):
    assert check_form(test_dict, test_lst) == expected_result
