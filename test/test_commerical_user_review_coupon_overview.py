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



#url = 'http://127.0.0.1:8000/v0/users/1/coupon_messages/' 
url = 'http://127.0.0.1:8000/v0/users/1/coupon_messages?option=overview' 

'''
TODO: implement store features.
'''

params = {
            #'store_id': '',
            #'user_id': 1,
            'method': 'read',
            #'option': 'overview',
            'offset': 80,
            'limit': 10
          }

cookie = {'sessionid': 'p0jeltx41hc3rn6pgk2w8hg6cmpw9bag'}

headers = {
              #'Content-Type': 'application/x-www-form-urlencoded',
              #'content-type' : 'application/json',
              #'Content-Type': 'multipart/form-data',
              'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6Ik5qTTNRVE14TTBaRVJEYzJRVEpGUlVORE9UaEROa1ZDUmpnek5UWTBRVFZHTXpJMk4wTkVNZyJ9.eyJpc3MiOiJodHRwczovL2RyZWFtZXIyMDE4LXByb3RvdHlwZS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWJhYzMzMmM5NjMxYTMzMjFkNGY0MjM0IiwiYXVkIjoiVGVzdCBBUEkiLCJpYXQiOjE1NDc5NDk5ODYsImV4cCI6MTU0ODAzNjM4NiwiYXpwIjoidlphX3hzZGd3QWFyMEtpUDlteS1HM2RzS3Q1a0J1QlkiLCJndHkiOiJwYXNzd29yZCJ9.o5SFXIu-6K5ivqMBL6mSPuAy4tfNZZ7zH1TP_DQKWUhQ01cNi3WZef3Dv-01rJp1POhEjb-LubiOcEyAJCXiB3WrmpdEVfEUkXGz6C4MDE1Vlfk4gr-1gog3GiWeIalv9B7nP4-0CUB8sou9xWcFPQSRHeL17SVNt9wetW0P97JTjkX_RwTew5b5O5EyTNk44_vrbAWH3P_g2iRCQbfyyvwCj2qev-6-ClF9Kcoe2AHCtmN_fcjzmxg9DBJ9B-dW3A2awCvj5Z_tFU9VR5QHlh6comaHVykqVNUCTVkBg4we93R3ucYf6fydTFss8GJP0SxTy6PW_qS002-FpNiJSg'
          }

files = {}

 
r = requests.get(
        url,
        cookies = cookie,
        params = params,
        headers = headers,
        files = files,
)

print(r.text)