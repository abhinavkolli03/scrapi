from playwright.async_api import async_playwright
import asyncio
import json

async def main():
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(
            headless=False
        )
        
        page = await browser.new_page()
        await page.goto('https://www.amazon.com/b?node=17938598011')
        await page.wait_for_timeout(5000)
        
        all_products = await page.query_selector_all('.a-spacing-base')
        data = []
        for product in all_products:
            result = dict()
            
            title_el = await product.query_selector('span.a-size-base-plus')
            result['title'] = await title_el.inner_text()
            
            price_el = await product.query_selector('span.a-price')
            result['price'] = await price_el.inner_text()
            
            rating_el = await product.query_selector('span.a-icon-alt')
            result['rating'] = await rating_el.inner_text()

            data.append(result)
        
        with open("results.json", "w") as file:
            json.dump(data, file, indent=4)
            
        await browser.close()
        
        
if __name__ == '__main__':
    asyncio.run(main())