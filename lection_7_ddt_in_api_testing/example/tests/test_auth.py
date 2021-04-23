import requests
import pytest


def test_methods_availability(base_url, auth_availability):
    endpoint = auth_availability[0]
    method = auth_availability[1]
    expected_status = auth_availability[2]
    description = auth_availability[3]

    response = requests.request(method, f"{base_url}/auth/{endpoint}")

    assert response.status_code == int(expected_status), \
        f"Wrong status code on auth {endpoint} url for {method} method"

    assert response.json().get("description") == description
