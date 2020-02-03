import json
import requests

url = 'http://127.0.0.1:8000/v0/users/2/locations/' 

playload = {
            'latitude': '13.41156',
            'longitude': '52.522906',
            'time': '2018-07-10 15:04:21.962718-07'
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