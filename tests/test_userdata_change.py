import allure
import pytest
from data_to_test import TestData
from route_user import APIUser


class TestUserdataChange:
    @pytest.mark.parametrize('data_set',[{"email": "kukuruku2025@ku.ru","password": TestData.new_user["password"],"name": TestData.new_user["name"]},
                                         {"email": TestData.new_user["email"],"password": "7654321","name": TestData.new_user["name"]},
                                         {"email": TestData.new_user["email"],"password": TestData.new_user["password"],"name": "Kukuruku2025"}])
    @allure.title('Проверка изменения данных пользователя с авторизацией (параметризация)')
    def test_change_userdata_when_authorised(self, data_set):
        new_user= APIUser.create_user(TestData.new_user)
        access_token = new_user.json().get('accessToken')

        change_result = APIUser.change_userdata(data_set, access_token)
        with allure.step('Проверка кода ответа успешного изменения данных 200'):
            assert change_result.status_code == 200
            assert change_result.json().get('success') == True

        APIUser.delete_user(access_token)


    @pytest.mark.parametrize('data_set', [{"email": "kukuruku2025@ku.ru","password": TestData.new_user["password"],"name": TestData.new_user["name"]},
                                         {"email": TestData.new_user["email"],"password": "7654321","name": TestData.new_user["name"]},
                                         {"email": TestData.new_user["email"],"password": TestData.new_user["password"],"name": "Kukuruku2025"}])

    @ allure.title('Проверка изменения данных пользователя без авторизации (параметризация)')
    def test_change_userdata_when_not_authorised(self,data_set):
        new_user = APIUser.create_user(TestData.new_user)
        access_token = new_user.json().get('accessToken')

        change_result = APIUser.change_userdata(data_set, '')
        with allure.step('Проверка кода ошибки 401 и текста'):
            assert change_result.status_code == 401
            assert 'You should be authorised' in change_result.text

        APIUser.delete_user(access_token)
