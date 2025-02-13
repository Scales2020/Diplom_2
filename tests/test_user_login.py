import allure
from data_to_test import TestData
from route_user import APIUser


class TestUserLogin:
    @allure.title('Проверка авторизации под существующим пользователем')
    def test_login_existing_user_200(self):
        user_reg = APIUser.create_user(TestData.new_user)
        refresh_token = user_reg.json().get('refreshToken')
        access_token = user_reg.json().get('accessToken')

        user_login = APIUser.login_user(TestData.new_user, refresh_token)
        with allure.step('Код ответа при успешной авторизации 200'):
            assert user_login.status_code == 200
            assert user_login.json().get('success') == True

        APIUser.delete_user(access_token)

    @allure.title('Проверка авторизации с неверным логином и паролем')
    def test_login_with_incorrect_login_password(self):
        user_reg = APIUser.create_user(TestData.new_user)
        refresh_token = user_reg.json().get('refreshToken')
        access_token = user_reg.json().get('accessToken')

        user_login = APIUser.login_user(TestData.new_user_wrong, refresh_token)
        with allure.step('Код ошибки 401 и текст'):
            assert user_login.status_code == 401
            assert 'email or password are incorrect' in user_login.text

        APIUser.delete_user(access_token)
