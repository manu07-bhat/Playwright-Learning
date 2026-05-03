from playwright.sync_api import sync_playwright
with sync_playwright() as o:
    gg = o.chromium.launch(headless=False)
    page = gg.new_page()
    page.goto("https://blog.jetbrains.com")
    page.goto('https://www.google.com/'  )