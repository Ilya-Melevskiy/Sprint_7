import requests
import allure

from helpers.helpers import Help
from urls.urls import CREATE_COURIER

class TestCreateCourier:

    @allure.title('Создание курьера - получение кода 201 при корректном запросе')
    def test_create_courier_correct_data_return_201(self):
        help = Help()
        payload = help.generate_login_password_firstname()
        response = requests.post(CREATE_COURIER, json=payload)
        assert response.status_code == 201

    @allure.title('Создание курьера - получение корректного тела ответа при корректном запросе')
    def test_create_courier_correct_data_return_correct_body(self):
        help = Help()
        payload = help.generate_login_password_firstname()
        response = requests.post(CREATE_COURIER, json=payload)
        assert response.json() == {"ok":True}
    
    @allure.title('Создание курьера - получение кода 409 при создании дубля курьера')
    def test_create_courier_double_courier_return_409(self):
        help = Help()
        payload = help.generate_login_password_firstname()
        requests.post(CREATE_COURIER, json=payload)
        response = requests.post(CREATE_COURIER, json=payload)
        assert response.status_code == 409

    @allure.title('Создание курьера - получение корректного тела ответа при создании дубля курьера')
    def test_create_courier_double_courier_return_correct_body(self):
        help = Help()
        payload = help.generate_login_password_firstname()
        requests.post(CREATE_COURIER, json=payload)
        response = requests.post(CREATE_COURIER, json=payload)
        assert response.json()['message'] == 'Этот логин уже используется. Попробуйте другой.'
    
    @allure.title('Создание курьера - получение кода 400 при создании курьера без логина')
    def test_create_courier_without_login_return_400(self):
        help = Help()
        payload = {
            "login": '',
            "password": help.generate_password(),
            "firstName": help.generate_firstname()
        }
        response = requests.post(CREATE_COURIER, json=payload)
        assert response.status_code == 400
        
    @allure.title('Создание курьера - получение корректного тела ответа при создании курьера без логина')
    def test_create_courier_without_login_return_correct_body(self):
        help = Help()
        payload = {
            "login": '',
            "password": help.generate_password(),
            "firstName": help.generate_firstname()
        }
        response = requests.post(CREATE_COURIER, json=payload)
        assert response.json()['message'] == 'Недостаточно данных для создания учетной записи'

    @allure.title('Создание курьера - получение кода 400 при создании курьера без пароля')
    def test_create_courier_without_password_return_400(self):
        help = Help()
        payload = {
            "login": help.generate_login(),
            "password": '',
            "firstName": help.generate_firstname()
        }
        response = requests.post(CREATE_COURIER, json=payload)
        assert response.status_code == 400
        
    @allure.title('Создание курьера - получение корректного тела ответа при создании курьера без пароля')
    def test_create_courier_without_password_return_correct_body(self):
        help = Help()
        payload = {
            "login": help.generate_login(),
            "password": '',
            "firstName": help.generate_firstname()
        }
        response = requests.post(CREATE_COURIER, json=payload)
        assert response.json()['message'] == 'Недостаточно данных для создания учетной записи'

    @allure.title('Создание курьера - получение кода 409 при создании курьера с существующим логином')
    def test_create_courier_same_login_return_409(self):
        help = Help()
        login = help.generate_login()
        password = help.generate_password()
        first_name = help.generate_firstname()
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        requests.post(CREATE_COURIER, json=payload)
        new_password = help.generate_password()
        new_first_name = help.generate_firstname()
        payload_same_login = {
            "login": login,
            "password": new_password,
            "firstName": new_first_name
        }
        response = requests.post(CREATE_COURIER, json=payload_same_login)
        
        assert response.status_code == 409
        
    @allure.title('Создание курьера - получение корректного тела ответа при создании курьера с существующим логином')
    def test_create_courier_same_login_return_correct_body(self):
        help = Help()
        login = help.generate_login()
        password = help.generate_password()
        first_name = help.generate_firstname()
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        requests.post(CREATE_COURIER, json=payload)
        new_password = help.generate_password()
        new_first_name = help.generate_firstname()
        payload_same_login = {
            "login": login,
            "password": new_password,
            "firstName": new_first_name
        }
        response = requests.post(CREATE_COURIER, json=payload_same_login)
        
        assert response.json()['message'] == 'Этот логин уже используется. Попробуйте другой.'