# Мишагин Александр 18-я когорта QA+. Финальный проект.

import configuration
import requests

# создание заказа
def create_order(body):
    return requests.post (configuration.URL_OF_ORDERS + configuration.CREATE_ORDER,
                         json=body)

# получение заказа по трекеру
def getting_order(track_number):
    get_order_url = f"{configuration.URL_OF_ORDERS}{configuration.GET_ORDER}={track_number}"
    response = requests.get(get_order_url)
    return response