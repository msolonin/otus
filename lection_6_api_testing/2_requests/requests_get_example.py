import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts/1')

print("\n------- status/headers/encoding ---------")

print(response.status_code)
print(response.headers['content-type'])
print(response.encoding)

print("\n----------------- text ------------------")
print(response.text)
print("\n----------------- json ------------------")

print(response.json())

print("\n---------------- headers ----------------")

for key, value in response.headers.items():
    print(key, ' => ', value)
