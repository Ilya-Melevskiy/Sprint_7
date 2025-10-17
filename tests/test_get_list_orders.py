import requests
import allure

class TestCreateOrder:

    @allure.title('Получение списка заказов - возврат кода 200')
    def test_get_list_orders_return_200(self):
        response = requests.get(
            "https://qa-scooter.praktikum-services.ru/api/v1/orders"
        )

        assert response.status_code == 200

    @allure.title('Получение списка заказов - наличие ключа "orders" в теле ответа ')
    def test_get_list_orders_return_body_with_key_orders(self):
        response = requests.get(
            "https://qa-scooter.praktikum-services.ru/api/v1/orders"
        )

        assert "orders" in response.json()

    @allure.title('Получение списка заказов - наличие списка по ключу "orders" в теле ответа ')
    def test_get_list_orders_return_body_with_list_orders(self):
        response = requests.get(
            "https://qa-scooter.praktikum-services.ru/api/v1/orders"
        )

        assert type(response.json()["orders"]) is list 

    @allure.title('Получение списка заказов - список по ключу "orders" в теле ответа не пустой ')
    def test_get_list_orders_return_list_not_empty(self):
        response = requests.get(
            "https://qa-scooter.praktikum-services.ru/api/v1/orders"
        )

        assert len(response.json()["orders"]) 

