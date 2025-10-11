from playwright.sync_api import Page, expect

fakePayloadOrderResponse = {"data": [], "message": "No Orders"}


# api call from browser -> api call contact server return back response -> browser use response to generate html
def intercept_response(route):
    route.fulfill(
        json=fakePayloadOrderResponse
    )


def test_Network1(page: Page):
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept_response)
    page.get_by_placeholder("email@example.com").fill("test@fd.com")
    page.get_by_placeholder("enter your passsword").fill("Test@1234")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()
    expect(page.locator(".mt-4.ng-star-inserted")).to_have_text("You have No Orders to show at this time. Please Visit Back Us")
