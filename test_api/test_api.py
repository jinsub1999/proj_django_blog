import requests

HOST = 'http://127.0.0.1:8000'

res = requests.post("http://127.0.0.1:8000/api-token-auth/", { 'username':'---', 'password':'---',})

# print(res.json())
res.raise_for_status()
token = res.json()['token'] 
# print(token)

# 인증이 필요한 요청에 아래의 headers를 붙임
headers = {'Authorization' : 'JWT ' + token, 'Accept' : 'application/json'}
# Post Create
data = {  
    'title' : 'Test_API_제목',
    'text' : 'Test_API_내용',
    'created_date' : '2023-04-01T18:34:00+09:00',
    'published_date' : '2023-04-01T18:34:00+09:00'
}

file = {'image' : open('---.png', 'rb')}
res = requests.post(HOST + '/api_root/Post/', data=data, files=file, headers=headers) 

# print(res)
# print(res.json())