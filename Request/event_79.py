import json
import allure
from send_request import post_request


def included_in_consolidation(token, destinationPointId):
    url = 'http://events-backend-edu.pegasus.ponyex.local/api/v1/event-blocks79/post-item'
    headers = {'Authorization': f'Bearer {token}'}
    data = {"description":"","destinationPointId":destinationPointId}

    with allure.step('Создание блока событий - 79 включён в консолидацию'):
        r = post_request(url, json=data, headers=headers)

        return json.loads(r.text)

def add_object(token, id_, number):
    url = 'http://events-backend-edu.pegasus.ponyex.local/api/v1/pegasus-events79/post-item'
    headers = {'Authorization': f'Bearer {token}'}
    data = {
        "IsRouteValidationEnabled": False,
        "eventBlockId": id_,
        "pointId": "07c5c96a-6f52-428d-9332-0004c296067e",
        "scannedNumber": number,
        "hostname": "DESKTOP-M4BHSDU"
    }

    with allure.step('Добавления объекта с номером: ' + number):
        r = post_request(url, json = data, headers = headers)

        return json.loads(r.text)