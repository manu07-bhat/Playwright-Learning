import time,re

from playwright.sync_api import Page, expect

def test_verify_locators(page :Page):
    #get_by_alttext()
    page.goto('https://demo.nopcommerce.com/')
    time.sleep(5)
    page.wait_for_timeout(5000)
    logo = page.get_by_alt_text('nopCommerce demo store') # returns locators
    expect(logo).to_be_visible()
    expect(page.get_by_alt_text('nopCommerce demo store')).to_be_visible()

    #page.get_by_test('')
    expect(page.get_by_text('Welcome to our store')).to_be_visible() #full text
    expect(page.get_by_text('Welcome to ')).to_be_visible() #partial
    expect(page.get_by_text(re.compile('.*Welcome.*'))).to_be_visible()
