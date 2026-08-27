import random
import string

import requests

from urls import Urls


def generate_random_string(length: int) -> str:
    return ''.join(random.choices(string.ascii_lowercase, k=length))


def generate_user_data() -> dict:
    return {
        'email': f'{generate_random_string(10)}@yandex.ru',
        'password': generate_random_string(12),
        'name': generate_random_string(8)
    }


def register_user_via_api(user_data: dict) -> str:
    response = requests.post(Urls.API_REGISTER, json=user_data)
    return response.json().get('accessToken')


def delete_user_via_api(access_token: str):
    return requests.delete(Urls.API_USER, headers={'Authorization': access_token})