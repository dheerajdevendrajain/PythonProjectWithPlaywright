from .orderDetailsPage import OrderDetailsPage


class OrdersHistoryPage:

    def __init__(self, page):
        self.page = page

    def selectOrder(self, orderId):
        self.page.locator("tr").filter(has_text=orderId).get_by_role("button", name="view").click()
        orderDetailsPage = OrderDetailsPage(self.page)
        return orderDetailsPage
