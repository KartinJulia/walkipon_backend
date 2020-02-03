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

url = 'http://127.0.0.1:8000/v0/login/' 

playload = {
               "audience": "Test API",
               "client_id": "vZa_xsdgwAar0KiP9my-G3dsKt5kBuBY",
               "client_secret": "LzOyJcBFJ9TfT4vO6lAJVgohJMd9yxk91vsIt66jB9G5D1R0eqkkGDqEyBTReH5H",
               "email": "walkipon@gmail.com",
               "grant_type": "password",
               "password": "walkipon123",
               "username": "walkipon"
            }

headers = {"Content-Type": "application/json; charset=utf-8"}
 
r = requests.post(
        url,
        data = json.dumps(playload),
        headers = headers,
)
print(r.cookies)
print(r.text)