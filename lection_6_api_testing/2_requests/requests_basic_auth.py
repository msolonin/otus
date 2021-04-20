import requests

# Keep in mind that next request will not be made as authorized
# DOC: https://docs.python-requests.org/en/master/
response = requests.get('https://httpbin.org//basic-auth/user/password', auth=('user', 'password'))

print(response.text)
print(response.status_code)

