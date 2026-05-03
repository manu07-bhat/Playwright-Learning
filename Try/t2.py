from playwright.sync_api import Playwright, sync_playwright

with sync_playwright() as d1:
    browser = d1.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    print(page.title())
    print("title" + page.title())
    page.wait_for_timeout(500)

    name = page.wait_for_selector('input[name="username"]')
    name.type('Admin')
    pass1 = page.wait_for_selector('input[name="password"]')
    pass1.type('admin123')
    submit_button = page.wait_for_selector('button[type = submit]')
    submit_button.click()
    page.wait_for_timeout(500)
    print("done")