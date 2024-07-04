# Мишагин Александр 18-я когорта QA+. Финальный проект.

import configuration
import requests
import data

# создание заказа
def create_order(body):
    return requests.post (configuration.URL_OF_ORDERS + configuration.CREATE_ORDER,
                         json=body)

# получение заказа по трекеру
def getting_order(track_number):
    get_order_url = f"{configuration.URL_OF_ORDERS}/api/v1/orders/track?t={track_number}"
    response = requests.get(get_order_url)
    return response

# наш автотест
def test_creation_of_order_and_searching():
    response = create_order(data.order_body)

    track_number = response.json()["track"]
    print("Заказ создан. Номер трека:", track_number)

# получение данных заказа по треку
    order_response = getting_order(track_number)

# проверка, что код ответа равен 200
    assert order_response.status_code == 200, f"Ошибка: {order_response.status_code}"
    order_data = order_response.json()
    print("Данные заказа:")
    print(order_data)