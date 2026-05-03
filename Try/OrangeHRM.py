from playwright.sync_api import sync_playwright
with sync_playwright() as g:
    browser = g.chromium.launch (headless=False)
    page = browser.new_page()
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

    # Tagname | tagname[attribute = "value"]
    username = page.wait_for_selector('input[name="username"]')
    username.type('Admin')
    Passwd = page.wait_for_selector('input[name="password"]')
    Passwd.type('admin123')
    loginclk = page.wait_for_selector('button[type="submit"]')
    loginclk.click()
    page.wait_for_timeout(2000)

    print(page.title()+" URL "+page.url)
    print(f" title is '{page.title()}'")