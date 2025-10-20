import requests
import allure

from urls.urls import GET_LIST_ORDERS

class TestGetListOrders:

    @allure.title('Получение списка заказов - возврат кода 200')
    def test_get_list_orders_return_200(self):
        response = requests.get(
            GET_LIST_ORDERS
        )

        assert response.status_code == 200

    @allure.title('Получение списка заказов - наличие ключа "orders" в теле ответа ')
    def test_get_list_orders_return_body_with_key_orders(self):
        response = requests.get(
            GET_LIST_ORDERS
        )

        assert "orders" in response.json()

    @allure.title('Получение списка заказов - наличие списка по ключу "orders" в теле ответа ')
    def test_get_list_orders_return_body_with_list_orders(self):
        response = requests.get(
            GET_LIST_ORDERS
        )

        assert type(response.json()["orders"]) is list 

    @allure.title('Получение списка заказов - список по ключу "orders" в теле ответа не пустой ')
    def test_get_list_orders_return_list_not_empty(self):
        response = requests.get(
            GET_LIST_ORDERS
        )

        assert len(response.json()["orders"]) 

