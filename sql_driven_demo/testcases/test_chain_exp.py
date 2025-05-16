
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import requests
from utils.logger import logger

def test_login_wrong_password():
    data = {"email": "nonexist@reqres.in", "password": "wrongpass"}
    r = requests.post("http://127.0.0.1:5000/login", json=data)
    assert r.status_code == 401
    logger.info("登录失败：错误密码，状态码 %s", r.status_code)

def test_user_info_no_token():
    r = requests.get("http://127.0.0.1:5000/user_info")
    assert r.status_code == 403
    logger.info("未带 token 请求 user_info，状态码 %s", r.status_code)

def test_user_info_wrong_token():
    headers = {"Authorization": "fake_token_123"}
    r = requests.get("http://127.0.0.1:5000/user_info", headers=headers)
    assert r.status_code == 403
    logger.info("伪造 token 请求 user_info，状态码 %s", r.status_code)

