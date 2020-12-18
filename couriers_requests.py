from get_request import get_request
import json
from log_out import Print

def get_courier_by_id(token, courier_id):
    Print('Find courier with id = ' + courier_id)

    r = get_request(token, 1, f'/api/v1/couriers/get-courier-by-id/ {courier_id}', {'id': courier_id})
    if r == -1:
        Print('Failed')
        return -1
    if r.status_code != 200:
        return -1
    #print(r['result'])
    r = json.loads(r.text)

    if r['result'] == None:
        Print('Cant find current courier')

    return r

def get_couriers(token, page_index, page_size, sort_direction=0, search=''):
    r = get_request(token, 1, '/api/v1/couriers/get-couriers',
                    {'PageIndex': page_index, 'PageSize': page_size, 'SortDirection': sort_direction, 'Search': search})

    if r == -1:
        return -1
    if r.status_code != 200:
        return -1

    r = json.loads(r.text)

    return r

