from Authorization import authorization_r
import event_71_requests
from log_out import Print



def request_9():
    Print('Request 9')

    token = authorization_r()

    if token == -1:
        Print('Request 9 failed')
        return -1

    r = event_71_requests.without_sorting_and_couriers(token)

    if r == -1:
        Print('Request 9 failed')
        return -1

    id_ = r['result']['id']

    if id_ != None:
        Print('Block created with id: ' + id_)
    else:
        Print('Request 9 failed')
        return -1

    number = "11-1111-1111"

    r = event_71_requests.add_object(token, id_, number)

    if r == -1 or r['result'] == None:
        Print('Can\'t added obj with number: ' + number)
        Print('Request 9 failed')
        return -1

    waybill_id = r['result']['id']

    r = event_71_requests.find_object(token, id_)

    if r == -1 or r['result'] == None:
        Print('Can\'t find added obj')
        Print('Request 9 failed')
        return -1

    for waybill in r['result']:
        if waybill['id'] == waybill_id:
            Print('Add obj with number: ' + number + ' and id: ' + waybill_id)
            Print('Success')
            return 'Success'

    Print('Can\'t find obj with number: ' + number + ' and id: ' + waybill_id)
    Print('Request 9 failed')
    return -1

if __name__ == "__main__":
    request_9()