import requests

from constants import Constants
from data_to_test import TestData


class APIOrder:
    def create_order_without_token(data):
        return requests.post(f'{Constants.URL}/api/orders',data=data)

    def create_order_with_token(data, tok):
        return requests.post(f'{Constants.URL}/api/orders',data=data, headers={'Authorization': f'{tok}'})

    def create_list_of_user_orders_with_token(tok):
        return requests.get(f'{Constants.URL}/api/orders', headers={'Authorization': f'{tok}'})

    def create_list_of_user_orders_without_token(self):
        return requests.get(f'{Constants.URL}/api/orders')




