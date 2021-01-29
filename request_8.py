from Authorization import authorization_r
from event_71_requests import without_sorting_and_couriers
from log_out import Print



def request_8():
    Print('Request 8')

    token = authorization_r()

    if token == -1:
        Print('Request 8 failed')
        return -1

    r = without_sorting_and_couriers(token)

    if r == -1:
        Print('Request 8 failed')
        return -1

    if r['result']['id'] != None:
        Print('Block was created, id: ' + r['result']['id'])
        Print('Success')
    else:
        Print('Request 8 failed')
        return -1

if __name__ == "__main__":
    request_8()