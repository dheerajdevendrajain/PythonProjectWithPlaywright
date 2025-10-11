from playwright.sync_api import Page, expect


def test_UIvalidationsDynamicScript(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions")
    page.get_by_role("button", name="Sign In").click()
    iphoneProduct = page.locator("app-card").filter(has_text="iphone X")
    iphoneProduct.get_by_role("button").click()
    nokiaProduct = page.locator("app-card").filter(has_text="Nokia Edge")
    nokiaProduct.get_by_role("button").click()
    page.get_by_text("Checkout").click()
    expect(page.locator(".media-body")).to_have_count(2)

def test_childWindowHandle(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    with page.expect_popup() as newPage_info:
         page.locator(".blinkingText").filter(has_text="Free Access to InterviewQues/ResumeAssistance/Material").click()
         childPage = newPage_info.value
         text = childPage.locator(".im-para.red").text_content()
         print(text)
         words = text.split("at ")
         email = words[1].split(" ")[0]
         print(email)
         assert email == "mentor@rahulshettyacademy.com"


