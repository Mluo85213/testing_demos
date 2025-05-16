import pytest
from playwright.sync_api import sync_playwright
import os
import logging
import csv

# ===== 设置日志系统 =====
os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    filename="logs/test_results.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ===== 读取测试数据（CSV） =====
test_data = []
with open("test_data.csv", newline="", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        test_data.append((row["username"], row["password"]))

# ===== 创建截图文件夹 =====
os.makedirs("screenshots", exist_ok=True)

# ===== 测试函数定义 =====
@pytest.mark.parametrize("username,password", test_data)
def test_login(username, password):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://practicetestautomation.com/practice-test-login/")
        page.fill("#username", username)
        page.fill("#password", password)
        page.click("#submit")

        try:
            page.wait_for_selector("text=Logged In Successfully", timeout=2000)
            assert "Logged In Successfully" in page.content()
            logging.info(f"✅ 登录成功 - 用户名: {username}")
        except Exception:
            screenshot_path = f"screenshots/login_failed_{username}.png"
            page.screenshot(path=screenshot_path)
            logging.error(f"❌ 登录失败 - 用户名: {username}，截图已保存：{screenshot_path}")
            assert False, f"登录失败：用户名 `{username}`，截图见 {screenshot_path}"
        finally:
            browser.close()
