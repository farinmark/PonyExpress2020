from Authorization import authorization_r
import event_71_requests
from log_out import Print

'''
'''

def request_10():
    Print('Request 10')

    token = authorization_r()

    if token == -1:
        Print('Request 10 failed')
        return -1

    r = event_71_requests.without_sorting_and_couriers(token)

    if r == -1:
        Print('Request 10 failed')
        return -1

    id_ = r['result']['id']

    if id_ != None:
        Print('Block created with id: ' + id_)
    else:
        Print('Request 10 failed')
        return -1

    number = "11-1111-1112"

    r = event_71_requests.add_object(token, id_, number)

    if r == -1:
        Print('Can\'t add number: ' + number)
        Print('Request 10 failed')
        return -1

    if r['metadata']['message'] == "$_OBJECT_NUMBER_NOT_VALID_$: 11-1111-1112":
        Print('System return error «Номер объекта не валидный»')
        Print('Request 10 success')
        return 'Success'
    else:
        Print('System add obj with: ' + number)
        Print('Request 10 failed')
        return -1

if __name__ == "__main__":
    request_10()