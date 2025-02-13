import allure
from data_to_test import TestData
from route_order import APIOrder
from route_user import APIUser


class TestListOfOrders:
    @allure.title('Проверка получения заказов конкретного пользователя (с авторизацией)')
    def test_orders_list_by_user_with_token_succeeds_200(self):
        new_user = APIUser.create_user(TestData.new_user)
        access_token = new_user.json().get('accessToken')
        APIOrder.create_order_with_token(TestData.ingr, access_token)

        result = APIOrder.create_list_of_user_orders_with_token(access_token)
        with allure.step('Проверка кода ответа успешного создания списка 200'):
            assert result.status_code == 200
            assert result.json().get('success') == True

        APIUser.delete_user(access_token)

    @allure.title('Проверка получения заказов конкретного пользователя (без авторизации)')
    def test_orders_list_by_user_without_token_fails_401(self):
        new_user = APIUser.create_user(TestData.new_user)
        access_token = new_user.json().get('accessToken')

        APIOrder.create_order_with_token(TestData.ingr, access_token)
        result = APIOrder.create_list_of_user_orders_without_token(self)
        with allure.step('Проверка кода ошибки 401 и текста'):
            assert result.status_code == 401
            assert 'You should be authorised' in result.text

        APIUser.delete_user(access_token)

