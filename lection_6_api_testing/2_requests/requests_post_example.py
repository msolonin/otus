import requests

# Run mitmproxy to show requests
proxies = {
    "http": "http://127.0.0.1:8080",
    "https": "http://localhost:8080",
}

data = {
    "title": "this_is_my_title",
    "body": "this is body text for this test request",
    "userId": 1,
}

headers = {
    "Content-type": "application/json; charset=UTF-8",
    # "MyCustomValue": "Value"
}

# json, data
response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    headers=headers,
    json=data,
    proxies=proxies,
    verify=False
)

print(response.text)
