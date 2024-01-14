# Гордеева Дарья, 12-я когорта - Финальный проект. Инженер по тестированию плюс

import data
import sender_stand_request


def get_track():
    response = sender_stand_request.post_new_order(data.order_body)
    order_track = response.json()['track']
    return order_track


def test_order():
    track = get_track()
    res = sender_stand_request.get_order(track)
    assert res.status_code == 200, f"Ошибка: {res.status_code}"
    order_data = res.json()
    print("Данные заказа:")
    print(order_data)
