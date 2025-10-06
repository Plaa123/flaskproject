import requests
# get 请求
# res= requests.get('http://127.0.0.1:5001/methods/')
# print(res.text)

# post
res= requests.post('http://127.0.0.1:5001/methods/')
print(res.text)