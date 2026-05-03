from playwright.sync_api import Page, expect


def test_Url(page :Page):
    page.goto('https://playwright.dev/python/docs/intro')
    # page.wait_for_timeout(3000)
    expect(page).to_have_url('https://playwright.dev/python/docs/intro')

def test_verifyTitle(page :Page):
    page.goto('https://playwright.dev/python/docs/intro')
    expect(page).to_have_title('Installation | Playwright Python')
