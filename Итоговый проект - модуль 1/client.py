"""Клиент демонстрирующий работу с сервисами.
"""

from urllib.request import urlopen, Request
import json

samples = {'x' : [[1,1],[2,1],[1,0]],
           'y' : [0,1,1]}

data = json.dumps(samples).encode('utf-8')

req = Request('http://localhost:8081',
              headers = {'Contest-Type' : 'application/json'},
              data = data, method = 'POST')

with urlopen(req) as resp:
  resp_bytes = resp.read()
resp_str = resp_bytes.decode('utf-8')
model_id = json.loads(resp_str)['id']

batch = { 'id' : model_id,
          'x' : [[0,1],[1,2]] }

data = json.dumps(batch).encode('utf-8')

req = Request('http://localhost:8082',
              headers = {'Contest-Type' : 'application/json'},
              data = data, method = 'POST')

with urlopen(req) as resp:
  resp_bytes = resp.read()
resp_str = resp_bytes.decode('utf-8')

print(json.loads(resp_str))