import requests
import allure

from helpers.helpers import Help
from data.data import DataCourier 
from urls.urls import LOGIN_COURIER

class TestLoginCourier:

    @allure.title('Логин курьера в системе - возврат кода 200 при логине с корректными данными')
    def test_login_courier_correct_data_return_200(self, create_courier):
        login_pass = create_courier
        payload = {'login': login_pass[0],
                   'password': login_pass[1]}
        response = requests.post(LOGIN_COURIER, json=payload)
        assert response.status_code == 200
        
    @allure.title('Логин курьера в системе - возврат корректного тела при логине с корректными данными')
    def test_login_courier_correct_data_return_correct_id(self):
        data = DataCourier()
        payload = {'login': data.login,
                   'password': data.password}
        response = requests.post(LOGIN_COURIER, json=payload)
        assert response.json()['id'] == data.id
        
    @allure.title('Логин курьера в системе - возврат кода 400 при логине без пароля')
    def test_login_courier_without_password_return_400(self, create_courier):
        login_pass = create_courier
        payload = {'login': login_pass[0],
                   'password': ''}
        response = requests.post(LOGIN_COURIER, json=payload)
        assert response.status_code == 400
        
    @allure.title('Логин курьера в системе - возврат корректного тела при логине без пароля')
    def test_login_courier_without_password_return_correct_body(self, create_courier):
        login_pass = create_courier
        payload = {'login': login_pass[0],
                   'password': ''}
        response = requests.post(LOGIN_COURIER, json=payload)
        assert response.json()['message'] == "Недостаточно данных для входа"
        
    @allure.title('Логин курьера в системе - возврат кода 400 при логине без логина')
    def test_login_courier_without_login_return_400(self, create_courier):
        login_pass = create_courier
        payload = {'login': '',
                   'password': login_pass[1]}
        response = requests.post(LOGIN_COURIER, json=payload)
        assert response.status_code == 400
        
    @allure.title('Логин курьера в системе - возврат корректного тела при логине без логина')
    def test_login_courier_without_login_return_correct_body(self, create_courier):
        login_pass = create_courier
        payload = {'login': '',
                   'password': login_pass[1]}
        response = requests.post(LOGIN_COURIER, json=payload)
        assert response.json()['message'] == "Недостаточно данных для входа"
        
    @allure.title('Логин курьера в системе - возврат кода 404 при логине с несуществующей парой')
    def test_login_courier_non_existent_couple_return_404(self):
        help = Help()
        payload = {'login': help.generate_login(),
                   'password': help.generate_password()}
        response = requests.post(LOGIN_COURIER, json=payload)
        assert response.status_code == 404
        
    @allure.title('Логин курьера в системе - возврат корректного тела при логине с несуществующей парой')
    def test_login_courier_non_existent_couple_return_correct_body(self):
        help = Help()
        payload = {'login': help.generate_login(),
                   'password': help.generate_password()}
        response = requests.post(LOGIN_COURIER, json=payload)
        assert response.json()['message'] == "Учетная запись не найдена"

    @allure.title('Логин курьера в системе - возврат кода 404 при логине с неподходящим паролем')
    def test_login_courier_incorrect_password_return_404(self, create_courier):
        login_pass = create_courier
        payload = {'login': login_pass[0],
                   'password': '123'}
        response = requests.post(LOGIN_COURIER, json=payload)
        assert response.status_code == 404

    @allure.title('Логин курьера в системе - возврат корректного тела при логине с неподходящим паролем')
    def test_login_courier_incorrect_password_return_correct_body(self, create_courier):
        login_pass = create_courier
        payload = {'login': login_pass[0],
                   'password': '123'}
        response = requests.post(LOGIN_COURIER, json=payload)
        assert response.json()['message'] == "Учетная запись не найдена"