import pytest
from data_to_test import TestData
from route_user import APIUser


class TestUserdataChange:
    @pytest.mark.parametrize('data_set',[{"email": "kuku2025@ku.ru","password": "123456","name": "Kuku22"},
                                         {"email": "kuku22@ku.ru","password": "123456789","name": "Kuku22"},
                                         {"email": "kuku22@ku.ru","password": "123456","name": "Kuku2025"}])

    def test_change_userdata_when_authorised(self, data_set):
        new_user= APIUser.create_user(TestData.new_user)
        access_token = new_user.json().get('accessToken')

        change_result = APIUser.change_userdata(data_set, access_token)
        assert change_result.status_code == 200

        cleaning = APIUser.delete_user(access_token)
        print(cleaning.text)

    @pytest.mark.parametrize('data_set', [{"email": "kuku2025@ku.ru", "password": "123456", "name": "Kuku22"},
                                          {"email": "kuku22@ku.ru", "password": "123456789", "name": "Kuku22"},
                                          {"email": "kuku22@ku.ru", "password": "123456", "name": "Kuku2025"}])
    def test_change_userdata_when_not_authorised(self,data_set):
        new_user = APIUser.create_user(TestData.new_user)
        access_token = new_user.json().get('accessToken')

        change_result = APIUser.change_userdata(data_set, '')
        assert change_result.status_code == 401
        assert 'You should be authorised' in change_result.text

        cleaning = APIUser.delete_user(access_token)
        print(cleaning.text)
