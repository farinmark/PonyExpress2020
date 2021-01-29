from Authorization import authorization_r
import event_79_requests
from log_out import Print
import Pathes

'''
'''


def request_13():
    Print('Request 13')

    token = authorization_r()

    if token == -1:
        Print('Request 13 failed')
        return -1

    destinationPointId = Pathes.destinationPointId_1202

    r = event_79_requests.included_in_consolidation(token, destinationPointId)

    if r == -1:
        Print('Request 13 failed')
        return -1

    destinationPoint = r['result']['destinationPoint']

    if destinationPoint['code'] == '1202':
        Print('Block created')
        Print('Success')
        return 'Success'
    else:
        Print('Was added in different block')
        Print('Request 13 failed')
        return -1

if __name__ == "__main__":
    request_13()