from playwright.sync_api import sync_playwright
import csv
import logging
from datetime import datetime

logging.basicConfig(
    filename='test_results.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


class LoginTest:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def run(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto("https://practicetestautomation.com/practice-test-login/")

            page.fill("#username", self.username)
            page.fill("#password", self.password)
            page.click("#submit")

            try:
                page.wait_for_selector("text=Logged In Successfully", timeout=3000)
                assert "Logged In Successfully" in page.content()
                print(f"✅ 用户名 '{self.username}' 登录成功")
                logging.info(f"Login success - Username: {self.username}")
            except:
                page.screenshot(path=f"login_failed_{self.username}.png")
                print(f"❌ 用户名 '{self.username}' 登录失败，已截图保存")
                logging.error(f"Login failed - Username: {self.username}")
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                page.screenshot(path=f"login_failed_{self.username}_{timestamp}.png")


            browser.close()

if __name__ == "__main__":
   raw_data = [
    {"username": "student", "password": "Password123"},
    {"username": "student", "password": "wrongpassword"},
]

tests = []
with open("./test_data.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        tests.append(LoginTest(row["username"], row["password"]))


for test in tests:
    test.run()

