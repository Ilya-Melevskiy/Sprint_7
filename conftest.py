import pytest
import requests

from helpers.helpers import Help

@pytest.fixture
def create_courier():
    help = Help()
    login_pass =help.register_new_courier_and_return_login_password()

    yield login_pass

    payload = {'login': login_pass[0],
                'password': login_pass[1]}
    response_post = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', json=payload)
    id = response_post.json()['id']
    requests.delete(f"https://qa-scooter.praktikum-services.ru/api/v1/courier/{id}")


