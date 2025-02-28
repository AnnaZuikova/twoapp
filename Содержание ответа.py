import requests
response=requests.post("https://vk.com/api/v1/breeds/1")
print(response.headers.get("Content-Type"))
print(response.json())
