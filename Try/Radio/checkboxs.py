from playwright.sync_api import sync_playwright

with sync_playwright() as d:
    browser = d.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demo.automationtesting.in/Register.html")

    #Radiobutton
    radio_button = page.query_selector('//input[@value="FeMale"]')
    radio_button.click()
    # radio_button.check()
    # page.query_selector('//input[@value="Male"]').click()
    page.wait_for_timeout(3000)


    #checkbox
    page.query_selector('//input[@id="checkbox1"]').click()

    if radio_button.is_checked():
        print('Pass')
    else:
        print('Fail')
