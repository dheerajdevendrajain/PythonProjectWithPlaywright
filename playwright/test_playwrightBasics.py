import time

from playwright.sync_api import Page, expect, Playwright


def test_playwrightBasics(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://google.com")


#chromium headless mode, 1 single context
def test_playwrightShortcut(page:Page):
    page.goto("https://rahulshettyacademy.com/")

#python -m pytest test_playwrightBasics.py::test_playwrightShortcut --headed

def test_coreLocators(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions")
    page.get_by_role("button", name="Sign In").click()
    time.sleep(5)

def test_coreLocators_incorrectPassword(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning456")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions")
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()


def test_firefoxBrowser(playwright:Playwright):
    firefoxbrowser = playwright.firefox.launch(headless=False)
    page = firefoxbrowser.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions")
    page.get_by_role("button", name="Sign In").click()
    time.sleep(5)

