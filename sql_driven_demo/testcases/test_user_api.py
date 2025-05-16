import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import requests
from utils.db_utils import get_user_info
from utils.logger import logger

def test_user_api():
    logger.info("开始执行 user_info 接口测试")
    res = requests.get("http://127.0.0.1:5000/user_info?id=1")
    assert res.status_code == 200

    api_data = res.json()
    db_data = get_user_info(1)
    
    api_data = res.json()
    db_data = get_user_info(1)
    
    print("接口返回：", api_data)
    print("数据库返回：", db_data)
    

    assert api_data["email"] == db_data["email"]
    logger.info("测试通过：数据库与接口返回一致")
