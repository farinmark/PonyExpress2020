from get_request import get_request
import json
from log_out import Print
import Pathes


def get_condition_parameters(token):

    r = get_request(token, 12, '/api/v1/condition-parameters/get-all')

    if r == -1:
        return -1
    if r.status_code != 200:
        return -1

    r = json.loads(r.text)

    return r

def print_condition_parameters(token):
    r = get_condition_parameters(token)

    code_list = r['result']

    out = 'codes = [\n'

    for code in code_list:
        out += '[' + str(code['code']) + ', ' + "'" + code['name'] + "'" + '],\n'

    out += ']'

    Print(out)
    return 0