import allure
from data_to_test import TestData
from route_user import APIUser


class TestUserCreate:
    @ allure.title('Проверка создания уникального пользователя')
    def test_create_new_user_success_200(self):
        result = APIUser.create_user(TestData.new_user)
        with allure.step('проверяем, что код 200, а также сгенерированы accessToken и refreshToken'):
            assert result.status_code == 200
            assert 'accessToken' in result.text
            assert 'refreshToken' in result.text

        access_token = result.json().get('accessToken')
        APIUser.delete_user(access_token)

    @ allure.title("Проверяем создание пользователя, который уже зарегистрирован")
    def test_create_existing_user_failed_with_403(self):
        result = APIUser.create_user(TestData.new_user)

        with allure.step('Пытаемся создать уже созданного юзера, проверяем код ошибки 403 и текст'):
            result2 = APIUser.create_user(TestData.new_user)
        assert result2.status_code == 403
        assert "User already exists" in result2.text

        access_token = result.json().get('accessToken')
        APIUser.delete_user(access_token)

    @ allure.title('Проверка создания пользователя с незаполненным одним из обязательных полей (email)')
    def test_create_new_user_empty_email_failed_with_403(self):
        result = APIUser.create_user(TestData.user_empty_email)
        with allure.step('Проверяем код ошибки 403 и текст'):
            assert result.status_code == 403
            assert "Email, password and name are required fields" in result.text

        access_token = result.json().get('accessToken')
        APIUser.delete_user(access_token)




