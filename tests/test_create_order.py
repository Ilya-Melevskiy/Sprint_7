import requests
import allure
import pytest

class TestCreateOrder:

    @pytest.mark.parametrize('color', ['"BLACK"', '"GREY"', '"BLACK", "GREY"', ''])
    def test_create_order_color_black_or_grey_201(self, color):
        allure.dynamic.title(f"Создание заказа - получение кода 201 при создании заказа с цветом: {color}")
        payload = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": [color],
        }
        response = requests.post(
            "https://qa-scooter.praktikum-services.ru/api/v1/orders", json=payload
        )

        assert response.status_code == 201

    @allure.title('Создание заказа - возврат корректного тела при создании заказа с корректными данными')
    def test_create_order_correct_data_return_correct_body(self):
        payload = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": ["BLACK"],
        }
        response = requests.post(
            "https://qa-scooter.praktikum-services.ru/api/v1/orders", json=payload
        )

        assert "track" in response.json() and type(response.json()["track"]) is int
