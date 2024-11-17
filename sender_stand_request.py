# Импорт настроек из модуля configuration, который содержит параметры конфигурации, такие как URL сервиса
import configuration

# Импорт библиотеки requests для выполнения HTTP-запросов
import requests

# Импорт данных запроса из модуля data, в котором определены заголовки и тело запроса
import data

# создание заказа
def my_F():
    order_r = requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
    json=data.order_body)
    return order_r.json().get("track")

# Запрос на получение заказа по треку заказа
def get_order(track_order):
    return requests.get(configuration.URL_SERVICE+configuration.PUT_ORDER,
                        params=track_order)