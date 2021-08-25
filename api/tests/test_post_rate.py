import requests
import json

def test_post_rate():
    url = 'https://netguru-cars-api-kalek.herokuapp.com/rate/'
    car_id = 1
    rating = 5

    payload = {'car_id': car_id, 'rating': rating}
    headers = {'Content-Type': 'application/json;charset=UTF-8'}

    resp = requests.post(url, headers=headers, data=json.dumps(payload))

    assert resp.status_code == 200
