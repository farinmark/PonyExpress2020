import requests
import json
from log_out import Print


def get_all_groups(token):
    url = 'http://srv-pnew-01-test.ponyex.local:1001/api/v1/user-profile-groups/get-limit/1000'

    r = requests.get(url, headers = {'Authorization': f'Bearer {token}'})

    if r.status_code != 200:
        Print('Return Failed')
        return -1
    else:
        Print('Return Success')

    return json.loads(r.text)

def create_group(token, name):
    url = 'http://srv-pnew-01-test.ponyex.local:1001/api/v1/user-profile-groups/post-item'
    headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type':'application/json'
    }
    data = {'displayName':name}

    r = requests.post(url, json = data, headers = headers)

    if r.status_code != 200:
        Print('Return Failed')
        return -1
    else:
        Print('Return Success')

    return json.loads(r.text)

def delete_group(token, id):
    url = 'http://srv-pnew-01-test.ponyex.local:1001/api/v1/user-profile-groups/delete-item'
    headers = {'Authorization': f'Bearer {token}'}
    params = {'id': id}



    r = requests.delete(url, headers = headers, params = params)

    if r.status_code != 200:
        Print('Return Failed')
        return -1
    else:
        Print('Return Success')

    return json.loads(r.text)