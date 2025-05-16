import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
import requests
import logging
import csv

# ===== 日志配置 =====
from utils.logger import setup_logger
setup_logger("logs/test_results.log")

# ===== 读取测试数据 =====
test_data = []
base_dir = os.path.dirname(os.path.dirname(__file__)) 
data_file = os.path.join(base_dir, 'data', 'test_data.csv')
with open(data_file, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        test_data.append((row["username"], row["password"]))

# ===== 接口测试用例 =====
@pytest.mark.parametrize("username,password", test_data)
def test_login_api(username, password):
    url = "https://reqres.in/api/login"  # ❗替换为你的真实接口
    payload = {
    "email": username,   # 注意：reqres 用的是 email 字段，不是 username
    "password": password
}

    try:
        response = requests.post(url, json=payload)
        assert response.status_code == 200, f"状态码错误：{response.status_code}"
        json_data = response.json()
        assert "token" in json_data, f"登录失败：返回中没有 token 字段：{json_data}"
        logging.info(f"✅ 登录成功 - 用户名：{username}")
    except Exception as e:
        logging.error(f"❌ 登录失败 - 用户名：{username} - 错误信息：{str(e)}")
        assert False, str(e)
