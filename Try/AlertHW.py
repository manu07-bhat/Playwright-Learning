from playwright.sync_api import sync_playwright

text_alert = []

def handle_dialog(dialog):
    message = dialog.type
    text_alert.append(message)
    dialog.accept()

with sync_playwright() as g:
    browser = g.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demo.automationtesting.in/Alerts.html")

    page.on("dialog",handle_dialog)
    page.wait_for_selector('//a[@href="#Textbox"]').click()
    page.wait_for_selector('//div[@id="Textbox"]/button').click()
    page.wait_for_timeout(2000)
    print(text_alert[0])