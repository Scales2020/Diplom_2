from data_to_test import TestData
from route_user import APIUser


class TestUserCreate:
    def test_create_new_user_success_200(self):
        result = APIUser.create_user(TestData.new_user)
        assert result.status_code == 200
        assert 'accessToken' in result.text
        assert 'refreshToken' in result.text

        access_token = result.json().get('accessToken')
        cleaning = APIUser.delete_user(access_token)
        print(cleaning.text)

    def test_create_existing_user_failed_with_403(self):
        result = APIUser.create_user(TestData.new_user)
        assert result.status_code == 200

        result2 = APIUser.create_user(TestData.new_user)
        assert result2.status_code == 403
        assert "User already exists" in result2.text

        access_token = result.json().get('accessToken')
        cleaning = APIUser.delete_user(access_token)
        print(cleaning.text)

    def test_create_new_user_empty_email_failed_with_403(self):
        result = APIUser.create_user(TestData.user_empty_email)
        assert result.status_code == 403
        assert "Email, password and name are required fields" in result.text

        access_token = result.json().get('accessToken')
        cleaning = APIUser.delete_user(access_token)
        print(cleaning.text)




