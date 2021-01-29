from Authorization import authorization_r
import event_71_requests
from log_out import Print

'''
'''

def request_11():
    Print('Request 11')

    token = authorization_r()

    if token == -1:
        Print('Request 11 failed')
        return -1

    r = event_71_requests.without_sorting_and_couriers(token)

    if r == -1:
        Print('Request 11 failed')
        return -1

    id_ = r['result']['id']

    if id_ != None:
        Print('Block created with id: ' + id_)
    else:
        Print('Request 11 failed')
        return -1

    number = "0012345666"

    r = event_71_requests.add_object(token, id_, number)

    if r == -1:
        Print('Can\'t edit number: ' + number)
        Print('Request 11 failed')
        return -1

    if r['metadata']['message'] == "$_MARK_IS_NOT_BOUND_$":
        Print('System return error «Марка не привязана»')
        Print('Success')
        return 'Success'
    else:
        Print('System add ibj with number: ' + number)
        Print('Request 11 failed')
        return -1

if __name__ == "__main__":
    request_11()