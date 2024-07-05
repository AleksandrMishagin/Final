# Мишагин Александр 18-я когорта QA+. Финальный проект.

from sendor_stand_request import create_order, getting_order
import data

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

test_creation_of_order_and_searching()