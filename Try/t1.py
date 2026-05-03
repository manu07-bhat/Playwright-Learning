from playwright.sync_api import sync_playwright

with sync_playwright() as t1:
    browser = t1.chromium.launch(headless=False)
    page = browser.new_page() # chrome new tab
    page.goto("https://blog.jetbrains.com/pycharm/category/livestreams/") # nav page link
    page.wait_for_timeout(5000) # wait timer 5 sec
    print(page.title) # display the title
    print('Chrome launched successfully') # console o/p print