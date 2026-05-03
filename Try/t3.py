from playwright.sync_api import sync_playwright

with sync_playwright() as p:
     bro = p.chromium.launch(headless=False)
     page = bro.new_page()
     page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
     # page.title = "Google11111111s"
     # print(page.title)
     # Xpath - Relative
     user = page.wait_for_selector('//input[@name="username"]')
     user.type('Admin')
     pwd = page.wait_for_selector('//input[@placeholder="Password"]')
     pwd.type('admin1234')
     login = page.wait_for_selector('//button[@type="submit"]')
     login.click()
     if page.wait_for_selector('//*[text() = "Invalid credentials"]'):
         invalid = page.wait_for_selector('//p[text() = "Forgot your password? "]')
         invalid.click()
         username = page.wait_for_selector('//input[@name="username"]')
         username.type('manoj')
         reset = page.wait_for_selector('//button[@type="submit"]')
         reset.click()
         page.wait_for_timeout(10000)
     else:
        print("Password is valid")

     # xpathText
