import requests
response=requests.get("https://vk.com/v1/breeds")
print(response)
request=response.request
print(request)

print(response.status_code)
print(request.headers)