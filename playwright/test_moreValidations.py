import time

from playwright.sync_api import Page, expect


def test_UICheck(page: Page):
    # hide/ display functionalities
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button", name='Hide').click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()

    # Mouse Hover
    page.locator("#mousehover").hover()
    page.get_by_role("link", name="Top").click()

    # Alert boxes handling
    page.on("dialog", lambda dialog: dialog.accept())
    page.get_by_role("button", name='Confirm').click()
    time.sleep(3)

    # frame handling
    pageFrame = page.frame_locator("#courses-iframe")
    pageFrame.get_by_role("link", name="All Access plan").click()
    expect(pageFrame.locator("body")).to_contain_text("Happy Subscibers")

    # check the price of rice is 37
    # identify the price column
    # identify rice row
    # extract the price of the rice
    # table handling
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    for index in range(page.locator("th").count()):
        if page.locator("th").nth(index).filter(has_text="Price").count() > 0:
            colValue = index
            print(f"Price column value is: {colValue}")
            break
    riceRow = page.locator("tr").filter(has_text="Rice")
    expect(riceRow.locator("td").nth(colValue)).to_contain_text("37")
