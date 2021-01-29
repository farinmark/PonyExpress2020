from Authorization import authorization_r
import event_71_requests
from log_out import Print
'''
'''

def request_12():
    Print('Request 12')

    token = authorization_r()

    if token == -1:
        Print('Request 12 failed')
        return -1

    r = event_71_requests.without_sorting_and_couriers(token)

    if r == -1:
        Print('Request 12 failed')
        return -1

    id_ = r['result']['id']

    if id_ != None:
        Print('Block created with id: ' + id_)
    else:
        Print('Request 12 failed')
        return -1

    number = "11-1111-1111"

    r = event_71_requests.add_object(token, id_, number)

    if r == -1 or r['result'] == None:
        Print('Can\'t add obj with number: ' + number)
        Print('Request 12 failed')
        return -1

    waybill_id = r['result']['id']

    r = event_71_requests.find_object(token, id_)

    if r == -1 or r['result'] == None:
        Print('Can\'t find added obj')
        Print('Request 12 failed')
        return -1

    find = 0

    for waybill in r['result']:
        if waybill['id'] == waybill_id:
            find = 1
            break

    if find:
        Print('Add obj with number: ' + number + ' and id: ' + waybill_id)
    else:
        Print('Can\'t find obj with number: ' + number + ' and id: ' + waybill_id)
        Print('Request 12 failed')
        return -1

    r = event_71_requests.delete_object(token, waybill_id)

    if r == -1:
        Print('Request 12 failed')
        return -1

    r = event_71_requests.find_object(token, id_)

    if r == -1 or r['result'] == None:
        Print('Can\'t find added obj')
        Print('Request 12 failed')
        return -1

    find = 0

    for waybill in r['result']:
        if waybill['id'] == waybill_id:
            find = 1
            break

    if find:
        Print('Obj with number: ' + number + ' and id: ' + waybill_id + ' wasn\'t deleted')
        Print('Request 12 failed')
        return -1
    else:
        Print('Obj with number: ' + number + ' and id: ' + waybill_id + ' was deleted')
        Print('Success')
        return 'Success'

if __name__ == "__main__":
    request_12()