from playwright.async_api import Page, expect, async_playwright
import pytest
# pre -req = install "pip install pytest-asyncio"
@pytest.mark.asyncio
async def test_asc():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("https://demo.automationtesting.in/asc")
        # await expect(page).to_have_url('https://playwright.dev/python/docs/intro')