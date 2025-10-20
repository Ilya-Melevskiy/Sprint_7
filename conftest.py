import pytest
import requests

from helpers.helpers import Help
from urls.urls import LOGIN_COURIER, DELETE_COURIER

@pytest.fixture
def create_courier():
    help = Help()
    login_pass =help.register_new_courier_and_return_login_password()

    yield login_pass

    payload = {'login': login_pass[0],
                'password': login_pass[1]}
    response_post = requests.post(LOGIN_COURIER, json=payload)
    id = response_post.json()['id']
    requests.delete(DELETE_COURIER.format(id=id))


