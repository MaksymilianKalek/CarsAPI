import requests
import json

def test_post_create():
    url = 'https://netguru-cars-api-kalek.herokuapp.com/cars/'
    make = 'Volkswagen'
    model = 'Passat'

    payload = {'make': make, 'model': model}
    headers = {'Content-Type': 'application/json;charset=UTF-8'}

    resp = requests.post(url, headers=headers, data=json.dumps(payload))

    assert resp.status_code == 201