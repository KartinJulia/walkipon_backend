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



url = 'http://127.0.0.1:8000/v0/users/1/coupon_messages/100' 

'''
TODO: implement store features.
'''

payload = {
            'title': 'Nikon camera 10% off.',
            'method': 'update',
            'option': 'modify',
            'text': 'Nikon camera 10% off before Dec.18, 2018.'
           }

cookie = {'sessionid': '40a9l0ohk9xqk4ye44zq1nm4lbbu6mhg'}

headers = {
              'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6Ik5qTTNRVE14TTBaRVJEYzJRVEpGUlVORE9UaEROa1ZDUmpnek5UWTBRVFZHTXpJMk4wTkVNZyJ9.eyJpc3MiOiJodHRwczovL2RyZWFtZXIyMDE4LXByb3RvdHlwZS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWJhYzMzMmM5NjMxYTMzMjFkNGY0MjM0IiwiYXVkIjoiVGVzdCBBUEkiLCJpYXQiOjE1NDc2MDQ1ODksImV4cCI6MTU0NzY5MDk4OSwiYXpwIjoidlphX3hzZGd3QWFyMEtpUDlteS1HM2RzS3Q1a0J1QlkiLCJndHkiOiJwYXNzd29yZCJ9.hrIj_Mp1rJHMwjCZFo9UuZIGMQFUMgArjMHoM8FU8JPYzS7FOE39_08HVnNfmPlH301-86cWS95V_4un5GR1vouv6pdK2QpyMGZG-8Upyl5tfLy8R9acs_yqb-zjxULs4PzOLyzTTc8KwzI1y4em1EJooGws2PwPjbS1EC0_tUjo_Gf6sYusrXmakD43euxr7MjL8dqxWchHZ0hj82FoQBmcaVXmbpmjiAi6O10KKCQxR9_bMhJ1ywHm3rvJFAQZYOM40TpR_-eOefVggJbRCmAo1HzvDwVhWxUr_zhWsmiHCSy6-RRWrXuA8PD7WeathCY0oIokPPWowgYK0mh2Cg'
          }

files = {
            'image': open('/Users/yangzhong/Downloads/printable-coupons.jpg', 'rb')
        }

 
r = requests.post(
        url,
        cookies = cookie,
        data = payload,
        headers = headers,
        files = files,
)
