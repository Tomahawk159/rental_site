import requests
from common.common_variable import URL_TG_API


def send_telegram_message(data):
    url = URL_TG_API

    response = requests.post(url, json=data)
    if response.status_code == 200:
        return True
    return False
