import urllib3
import json

url = 'https://arver.ir/'

class Connect:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    def send_request(self, method, data):
        data.update({'username': self.username, 'password': self.password})
        data = json.dumps(data)
        http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED')
        headers = {'Content-Type': 'application/json'}
        da = http.request('POST', url + method + '.php',body=data, headers=headers)
        get_d = da.data.decode('utf-8')
        return json.loads(get_d)