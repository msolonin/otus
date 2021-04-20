import requests


proxies = {
    "http": "http://127.0.0.1:8080",
    "https": "http://localhost:8080",
}
# You can create your own requests!
r = requests.request("OTHER", "https://my-api-examaple.herokuapp.com/api/info/about",
                     proxies=proxies,
                     verify=False)

print(r.headers)