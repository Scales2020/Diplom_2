from data_to_test import TestData
from route_user import APIUser


class TestUserLogin:
    def test_login_existing_user_200(self):
        user_reg = APIUser.create_user(TestData.new_user)
        print(user_reg.text)
        refresh_token = user_reg.json().get('refreshToken')
        access_token = user_reg.json().get('accessToken')

        user_login = APIUser.login_user(TestData.new_user, refresh_token)
        print(user_login.text)
        assert user_login.status_code == 200

        cleaning = APIUser.delete_user(access_token)
        print(cleaning.text)

    def test_login_with_incorrect_login_password(self):
        user_reg = APIUser.create_user(TestData.new_user)
        print(user_reg.text)
        refresh_token = user_reg.json().get('refreshToken')
        access_token = user_reg.json().get('accessToken')

        user_login = APIUser.login_user(TestData.new_user_wrong, refresh_token)
        print(user_login.text)
        assert user_login.status_code == 401
        assert 'email or password are incorrect' in user_login.text

        cleaning = APIUser.delete_user(access_token)
        print(cleaning.text)
