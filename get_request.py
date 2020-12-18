import requests
from Pathes import urls
from log_out import Print

def get_request(token, num, api, params = None):
    if params is None:
        try:
            r = requests.get(urls[num] + api, headers = {'Authorization': f'Bearer {token}'})
            if r.status_code != 200:
                Print(r.status_code)
                Print('Return failed')
                return r
            else:
                Print('return success')
                return r
        except:
            Print('Cant send request')
            return -1
    else:
        try:
            r = requests.get(urls[num] + api, headers = {'Authorization': f'Bearer {token}'}, params = params)
            if r.status_code != 200:
                Print(r.status_code)
                Print('Return failed')
            else:
                Print('return success')
                return r
        except:
            Print('Cant send request')
            return -1
    return r