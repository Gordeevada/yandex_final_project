import configuration
import requests
import data


def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body)


def get_order(order_track):
    get_order_url = f"{configuration.URL_SERVICE + configuration.GET_ORDER_PATH}?t={order_track}"
    return requests.get(get_order_url)
