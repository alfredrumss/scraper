# import nest_asyncio; nest_asyncio.apply()
import asyncio
from playwright.async_api import async_playwright
from sqlmodel import Session, select
from src.models.product import Product
from bs4 import BeautifulSoup

class SteamScraper:
    def __init__(self, url):
        self.base_url = url
        self.total_pages = 2

    async def scrape_site(self):
        async with async_playwright() as pw:
            browser = await pw.chromium.launch(headless=False)
            context = await browser.new_context(viewport={"width": 1920, "height": 1080})
            page = await context.new_page()

            await page.goto(self.base_url)
            await page.wait_for_load_state("domcontentloaded")
            # await page.wait_for_load_state('networkidle')

            # from home page to the pagination page
            await page.wait_for_selector('a.btnv6_blue_hoverfade', state='visible', timeout=5000)
            await page.click('a.btnv6_blue_hoverfade')
            await page.wait_for_load_state('networkidle')

            for _page in range(1, self.total_pages + 1):

                try:
                    page_selector = f'span.market_paging_pagelink:has-text("{str(_page+1)}")'
                    await page.click(page_selector)
                    await page.wait_for_load_state('networkidle')
                except Exception as e:
                    print(f"Error navigating to page {_page} due to {e}")
                    continue

                soup = BeautifulSoup(await page.content(), "html.parser")
                for item in soup.select("a.market_listing_row_link")[:2]:

                    try:
                        item_link = item.get('href')
                        item_page = await browser.new_page()
                        await item_page.goto(item_link)
                        await item_page.wait_for_load_state('networkidle')

                        # Extract item details using BeautifulSoup
                        item_content = await item_page.content()
                        soup = BeautifulSoup(item_content, 'html.parser')

                        # Extracting attributes
                        item_title = soup.select_one('h1.hover_item_name')
                        sale_price = soup.select_one('div.market_listing_largeimage img')

                        # Close the item page
                        await item_page.close()

                    except Exception as e:
                        print(f"Error scraping item {item.get('href')}: due to {e}")

                    await page.wait_for_timeout(1000)

                await page.wait_for_timeout(1000)

            await browser.close()

async def scrapper_init():
    base_url = "https://steamcommunity.com/market/"

    scraper = SteamScraper(base_url)
    await scraper.scrape_site()

# if __name__ == "__main__":
#     asyncio.run(scrapper_init())

