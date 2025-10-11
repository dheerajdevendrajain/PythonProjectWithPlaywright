import json
import pytest
from playwright.sync_api import Playwright
from pageObjects.login import LoginPage
from utils.apiBaseFramework import APIUtils

with open('D:\\workspace\\PythonProjectWithPlaywright\\playwright\\data\\credentials.json') as f:
    test_data = json.load(f)
    print(test_data)
    user_credentials_list = test_data['user_credentials']

@pytest.mark.smoke
@pytest.mark.parametrize('user_credentials', user_credentials_list)
def test_e2e_framework_web_api(playwright: Playwright, browserInstance, user_credentials):
    username = user_credentials['userEmail']
    password = user_credentials['userPassword']
    # browser = playwright.chromium.launch(headless=False)
    # context = browser.new_context()
    # page = context.new_page()

    api_utils = APIUtils()
    orderId = api_utils.createOrder(playwright, user_credentials)
    print(orderId)

    loginPage = LoginPage(browserInstance)
    loginPage.navigate()
    dashboardPage = loginPage.login(username, password)

    ordersHistoryPage = dashboardPage.selectOrdersNavLink()
    orderDetailsPage = ordersHistoryPage.selectOrder(orderId)

    orderDetailsPage.verifyOrderMessage()
