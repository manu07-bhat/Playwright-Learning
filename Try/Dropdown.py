from playwright.sync_api import sync_playwright

with sync_playwright() as b:
    bro1 = b.chromium.launch(headless=False)
    page = bro1.new_page()
    page.goto("https://demo.automationtesting. in/Register.html")
    #dropdown select
    # 1 way
    select = page.wait_for_selector('//select[@ng-model="Skill"]')
    select.select_option(label= 'Art Design')
    page.wait_for_timeout(3000)
    # 2 way
    # select = page.query_selector('//select[@ng-model="Skill"]')
    select.select_option(label= 'Certifications')
    page.wait_for_timeout(2000)

    #direct selecting a dropdown
    page.select_option('//select[@ng-model="Skill"]',label= 'Diagnostics')
    page.wait_for_timeout(2000)