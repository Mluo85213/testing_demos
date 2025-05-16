import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import requests
from utils.logger import logger

def test_register_login_query(base_url, registered_user):
    reg_data = registered_user

    # 注册用户
    reg_data = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
    r1 = requests.post(f"{base_url}/register", json=reg_data)
    assert r1.status_code == 200
    logger.info("注册成功，响应：%s", r1.json())

    # 登录
    r1 = requests.post(f"{base_url}/login", json=reg_data)
    assert r1.status_code == 200
    token = r1.json()["token"]

    # 查询
    headers = {"Authorization": token}
    r2 = requests.get(f"{base_url}/user_info", headers=headers)
    assert r2.status_code == 200
    assert r2.json()["email"] == reg_data["email"]