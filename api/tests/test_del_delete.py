import requests

def test_del_delete():
    id = 10
    url = f'https://netguru-cars-api-kalek.herokuapp.com/cars/{id}/'

    headers = {'Content-Type': 'application/json;charset=UTF-8'}

    resp = requests.delete(url, headers=headers)

    assert resp.status_code == 204
