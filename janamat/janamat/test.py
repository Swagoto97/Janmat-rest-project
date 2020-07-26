print('hello')
import requests

url = 'http://127.0.0.1:8000/api/hello/'
headers = {'Authorization': 'Token 73a41d312855c9a3b3ce8e8f60caee941dbd3d3a'}
r = requests.get(url, headers=headers)
print(r)