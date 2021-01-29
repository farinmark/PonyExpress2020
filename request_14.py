from Authorization import authorization_r
import event_79_requests
from log_out import Print
import Pathes

'''
'''


def request_14():
    Print('Request 14')

    token = authorization_r()

    if token == -1:
        Print('Request 14 failed')
        return -1

    destinationPointId = Pathes.destinationPointId_1202

    r = event_79_requests.included_in_consolidation(token, destinationPointId)

    if r == -1 or r['result'] == None:
        Print('Can\'t created block of event 79')
        Print('Request 14 failed')
        return -1

    destinationPoint = r['result']['destinationPoint']

    if destinationPoint['code'] != '1202':
        Print('Was added in different block')
        Print('Request 14 failed')
        return -1

    Print('Block created')

    id_ = r['result']['id']

    number = "99-9999-9999/999"

    r = event_79_requests.add_object(token, id_, number)

    if r == -1:
        Print('Can\'t added number of obj')
        Print('Request 14 failed')
        return -1

    if r['metadata']['message'] == "$_PLACE_IS_OUT_OF_RANGE_$":
        Print('System return error «Отсутствует введенное место накладной»')
        Print('Success')
        return 'Success'
    else:
        Print('System find number of place of obj: ' + number)
        Print('Request 14 failed')
        return -1

if __name__ == "__main__":
    request_14()