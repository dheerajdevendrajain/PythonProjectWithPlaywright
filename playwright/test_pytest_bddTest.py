import pytest
from pyexpat import features
from pytest_bdd import given, when, then, parsers, scenarios

from pageObjects.login import LoginPage
from utils.apiBaseFramework import APIUtils

scenarios('features/OrderTransaction.feature')

@pytest.fixture
def shared_data():
    return {}


@given(parsers.parse('Place the item order with {username} and {password}'))
def place_item_order(playwright, username, password, shared_data):
    user_credentials = {}
    user_credentials['userEmail'] = username
    user_credentials['userPassword'] = password

    api_utils = APIUtils()
    orderId = api_utils.createOrder(playwright, user_credentials)
    print(orderId)
    shared_data['orderId'] = orderId


@given('The user is on landing page')
def user_is_on_landing_page(browserInstance, shared_data):
    loginPage = LoginPage(browserInstance)
    loginPage.navigate()
    shared_data['login_page'] = loginPage


@when(parsers.parse('I login to portal with {username} and {password}'))
def user_login_to_portal(username, password, shared_data):
    loginPage = shared_data['login_page']
    dashboardPage = loginPage.login(username, password)
    shared_data['dashboardPage'] = dashboardPage


@when('Navigate to orders page')
def navigate_to_orders_page(shared_data):
    dashboard_page = shared_data['dashboardPage']
    ordersHistoryPage = dashboard_page.selectOrdersNavLink()
    shared_data['orderHistory_page'] = ordersHistoryPage


@when('Select the orderId')
def select_order_id(shared_data):
    ordersHistoryPage = shared_data['orderHistory_page']
    orderId = shared_data['orderId']
    orderDetailsPage = ordersHistoryPage.selectOrder(orderId)
    shared_data['orderDetails_page'] = orderDetailsPage

@then('Order message is successfully displayed')
def order_message_successfully_displayed(shared_data):
    orderDetailsPage = shared_data['orderDetails_page']
    orderDetailsPage.verifyOrderMessage()