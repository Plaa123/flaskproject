import requests
# get 请求
res= requests.get('http://127.0.0.1:5001/request/?name=zhangsan&age=33&name=lisi&age=22',
cookies={'name':'hello'})
print(res.text)

# post
# res= requests.post('http://127.0.0.1:5001/request/',
#                    data= {'name':"lucy","age":20},
#                    cookies={'name':'hello'})
print(res.text)