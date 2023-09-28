from requests import Response

import data
import configuration
import requests

def post_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATING_AN_ORDER_PATH,
                         json=data.order_body, headers=data.headers)

def get_order_by_track(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_NUMBER_PATH,
           params={"t": track_number})

