# Импортируем модуль sender_stand_request, содержащий функции для отправки HTTP-запросов к API.
import sender_stand_request

# Импортируем модуль data, в котором определены данные, необходимые для HTTP-запросов.
import data

# Автотест
def positive_assert():
    track_response = sender_stand_request.get_order(data.params_get)
    assert track_response.status_code == 200


def test_order():
    data.params_get["t"] = sender_stand_request.my_F()
    positive_assert()

# Вера Нифонтова, 23-я когорта — Финальный проект. Инженер по тестированию расширенный