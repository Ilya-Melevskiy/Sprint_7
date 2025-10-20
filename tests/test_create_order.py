import requests
import allure
import pytest
from copy import deepcopy

from urls.urls import CREATE_ORDER 
from data.data import DataCustomer

class TestCreateOrder:

    @pytest.mark.parametrize('color', [["BLACK"], ["GREY"], ["BLACK", "GREY"], []])
    def test_create_order_color_black_or_grey_201(self, color):
        allure.dynamic.title(f"Создание заказа - получение кода 201 при создании заказа с цветом: {color}")
        payload = deepcopy(DataCustomer.payload)
        payload['color'] = color
        response = requests.post(
            CREATE_ORDER, json=payload
        )

        assert response.status_code == 201

    @allure.title('Создание заказа - возврат корректного тела при создании заказа с корректными данными')
    def test_create_order_correct_data_return_correct_body(self):
        payload = DataCustomer.payload
        response = requests.post(
            CREATE_ORDER, json=payload
        )

        assert "track" in response.json() and type(response.json()["track"]) is int
