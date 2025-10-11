from playwright.sync_api import Playwright

ordersPayload = {"orders": [{"country": "India", "productOrderedId": "68a961459320a140fe1ca57a"}]}


class APIUtils:

    def getToken(self, playwright: Playwright, userCredentials):
        user_name = userCredentials["userEmail"]
        user_password = userCredentials["userPassword"]
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com/")
        response = api_request_context.post("/api/ecom/auth/login",
                                            data={"userEmail": user_name, "userPassword": user_password})
        assert response.ok
        print(response.json())
        return response.json().get("token")

    def createOrder(self, playwright: Playwright, userCredentials):
        token = self.getToken(playwright, userCredentials)
        api_requestContext = playwright.request.new_context(base_url="https://rahulshettyacademy.com/")
        response = api_requestContext.post("api/ecom/order/create-order", data=ordersPayload,
                                           headers={"Authorization": token,
                                                    "Content-Type": "application/json"})
        print(response.json())

        response_body = response.json()
        orderId = response_body["orders"][0]
        return orderId
