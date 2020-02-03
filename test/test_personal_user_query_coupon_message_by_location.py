import json
import requests
from requests import Request
import ast
import logging

try:
    import http.client as http_client
except ImportError:
    import httplib as http_client
http_client.HTTPConnection.debuglevel = 1

# You must initialize logging, otherwise you'll not see debug output.
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True

url = 'http://127.0.0.1:8000/v0/users/2/coupon_messages/locations' 

playload = {
            'latitude': '38.1967403',
            'longitude': '-85.7305546',
            'radius':,
            'offset':,
            'limit':,
           }

cookie = {'sessionid': 'oxybqlkxreqkpt8izq93jvtfsfist5q0'}

headers = {
              'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6Ik5qTTNRVE14TTBaRVJEYzJRVEpGUlVORE9UaEROa1ZDUmpnek5UWTBRVFZHTXpJMk4wTkVNZyJ9.eyJpc3MiOiJodHRwczovL2RyZWFtZXIyMDE4LXByb3RvdHlwZS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWJhYzMzMmM5NjMxYTMzMjFkNGY0MjM0IiwiYXVkIjoiVGVzdCBBUEkiLCJpYXQiOjE1MzgwMTE5NzksImV4cCI6MTUzODA5ODM3OSwiYXpwIjoidlphX3hzZGd3QWFyMEtpUDlteS1HM2RzS3Q1a0J1QlkiLCJndHkiOiJwYXNzd29yZCJ9.SGQ6oX5qltTzgAihWPKqYhVWdRl60FC7JIWWSJSvzUQCz4qN223dooM9OLZ1tSpka-VpUXpork_nHfcp4hFbYPhyp9htS8-Og9eeyqxMzv75_Y75oC76ueWXNqAgZ8d-NTcpx57VNbCTMsKUIoMdPAi5QwjMgxWTjo5kCB-dqWCXVX9qfs-nJ2QbHf3xbsMa6XtI4SVPdOiblT07MEl1tghcr-TVhcyax5JaOsLAMxOaLwn0xRAw7FjOQqR5MvWtkQn7tgaR_Pin8BPMgQKWSwfxzJ09YLbdi-ifTu73Gnc8iGy0n_vzXJHkGZPJncMDhDe4fWU_YoiYFJ7mrgvFUQ'
          }

 
r = requests.post(
        url,
        cookies = cookie,
        data = playload,
        headers = headers,
)
#r.json()
print(r.text)