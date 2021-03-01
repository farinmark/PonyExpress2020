import json
import Pathes
from send_request import post_request
import requests
import allure

def authorisation(wrong = False):
    login = Pathes.correct_enter_login
    password = Pathes.correct_enter_password

    if wrong:
        login = Pathes.wrong_enter_login
        password = Pathes.wrong_enter_password

    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = {'username': login,
            'password': password,
            'grant_type': 'password',
            'scope': 'pegasus',
            'client_id': 'pegasus-v2',
            'client_secret': 'secret'}

    url = "http://srv-pnew-02-test:1001/auth/connect/token"

    if not wrong:
        with allure.step('Вход в систему'):

            r = post_request(url, headers = headers, data = data)

            answer = json.loads(r.text)

            return answer["access_token"]
    else:
        return requests.post(url, headers = headers, data = data)