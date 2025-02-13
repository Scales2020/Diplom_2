import allure
from data_to_test import TestData
from route_order import APIOrder
from route_user import APIUser


class TestOrderCreate:
    @ allure.title('Проверка создания заказа с авторизацией с ингредиентами')
    def test_order_create_when_authorised(self):
        new_user = APIUser.create_user(TestData.new_user)
        access_token = new_user.json().get('accessToken')

        result = APIOrder.create_order_with_token(TestData.ingr, access_token)
        with allure.step('Проверяем код результата 200'):
            assert result.status_code == 200
            assert result.json().get('success') == True


        APIUser.delete_user(access_token)

    @allure.title('Проверка создания заказа без авторизации с ингредиентами')
    def test_order_create_when_not_authorised(self):
        result = APIOrder.create_order_without_token(TestData.ingr)
        with allure.step('Проверяем код результата 200'):
            assert result.status_code == 200
            assert result.json().get('success') == True

    @allure.title('Проверка создания заказа без ингредиентов (с авторизацией)')
    def test_order_create_authorised_without_ingredients(self):
        new_user = APIUser.create_user(TestData.new_user)
        access_token = new_user.json().get('accessToken')

        result = APIOrder.create_order_with_token(TestData.ingr_empty, access_token)
        with allure.step('Проверяем код ошибки 400 и текст'):
            assert result.status_code == 400
            assert 'Ingredient ids must be provided' in result.text

        APIUser.delete_user(access_token)

    @allure.title('Проверка создания заказа без ингредиентов (без авторизации)')
    def test_order_create_unauthorised_without_ingredients(self):
        result = APIOrder.create_order_without_token(TestData.ingr_empty)
        with allure.step('Проверяем код ошибки 400 и текст'):
            assert result.status_code == 400
            assert 'Ingredient ids must be provided' in result.text

    @allure.title('Проверка создания заказа с неверным хешем ингредиентов (с авторизацией)')
    def test_order_create_authorised_with_nonvalid_ingredients(self):
        new_user = APIUser.create_user(TestData.new_user)
        access_token = new_user.json().get('accessToken')

        with allure.step(f'Создаем заказ с хешем {TestData.ingr_nonvalid}'):
            result = APIOrder.create_order_with_token(TestData.ingr_nonvalid, access_token)
        with allure.step('Проверяем код ошибки 500'):
            assert result.status_code == 500

        APIUser.delete_user(access_token)

    @allure.title('Проверка создания заказа с неверным хешем ингредиентов (без авторизации)')
    def test_order_create_unauthorised_with_nonvalid_ingredients(self):
        with allure.step(f'Создаем заказ с хешем {TestData.ingr_nonvalid}'):
            result = APIOrder.create_order_without_token(TestData.ingr_nonvalid)
        with allure.step('Проверяем код ошибки 500'):
            assert result.status_code == 500

