import requests
import json


def test_post_create():
    url = 'https://netguru-cars-api-kalek.herokuapp.com/popular/'

    headers = {'Content-Type': 'application/json;charset=UTF-8'}

    resp = requests.get(url, headers=headers)

    assert resp.status_code == 200
