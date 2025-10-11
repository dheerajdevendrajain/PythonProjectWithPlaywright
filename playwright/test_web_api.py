import json
import time

from playwright.sync_api import Playwright, expect

from utils.apiBase import APIUtils


def test_e2e_web_api(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    with open('D:\\workspace\\PythonProjectWithPlaywright\\playwright\\data\\credentials.json') as f:
        test_data = json.load(f)
        print(test_data)
        user_credentials_list = test_data['user_credentials']
    # create_order -> oderId
    api_utils = APIUtils()
    orderId = api_utils.createOrder(playwright)
    print(orderId)

    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill("test@fd.com")
    page.get_by_placeholder("enter your passsword").fill("Test@1234")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="Orders").click()
    page.locator("tr").filter(has_text=orderId).get_by_role("button", name="view").click()
    expect(page.locator(".tagline")).to_have_text("Thank you for Shopping With Us")
    time.sleep(5)
