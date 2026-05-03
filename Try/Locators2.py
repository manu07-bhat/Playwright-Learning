from playwright.sync_api import sync_playwright
with sync_playwright() as f:

    bro = f.chromium.launch(headless=False)
    page = bro.new_page()
    page.goto("https://demo.automationtesting.in/")
    page.wait_for_timeout(3000) # 3 sec hold
    #CSS Selector
        # id
    Emailtxt = page.wait_for_selector('#email')  # id base selector
    Emailtxt.type('test@gmail.com')
    page.click('#enterimg')
    page.wait_for_timeout(3000)  # 3 sec hold