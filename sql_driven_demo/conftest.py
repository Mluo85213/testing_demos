import pytest
import requests

@pytest.fixture(scope="session")
def base_url():
    return "http://127.0.0.1:5000"

@pytest.fixture(scope="function")
def registered_user(base_url):
    data = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
    requests.post(f"{base_url}/register", json=data)  # 注册一次
    return data
