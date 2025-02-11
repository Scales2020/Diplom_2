import requests

from constants import Constants


class APIUser:
    def create_user(data):
        return requests.post(f'{Constants.URL}/api/auth/register',data=data)

    def delete_user(tok):
        return requests.delete(f'{Constants.URL}/api/auth/user', headers={'Authorization': f'{tok}'})

    def login_user(data, tok):
        return requests.post(f'{Constants.URL}/api/auth/login', data = data, headers={'Authorization': f'{tok}'})

    def change_userdata(data, tok):
        return requests.patch(f'{Constants.URL}/api/auth/user', data=data, headers={'Authorization': f'{tok}'})

