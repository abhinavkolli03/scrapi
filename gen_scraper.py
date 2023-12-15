from playwright.async_api import async_playwright
import asyncio
import json

async def main():
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(
            headless=False
        )
        
        page = await browser.new_page()
        await page.goto('https://developer.paypal.com/api/rest/')
        await page.wait_for_timeout(5000)
        
        all_sections = await page.query_selector_all('section[id^="api-section"]')
        data = []
        print(len(all_sections))
            
        for sect in all_sections:
            
            section_data = {}
            checking_tags = ['h1', 'h2', 'code', 'p']
            
            for tag_name in checking_tags:
                tags = await sect.query_selector_all(tag_name)
                for i, tag in enumerate(tags, start = 1):
                    text = await tag.inner_text()
                    if text.strip():
                        section_data[f"{tag_name} {i}"] = text
                    
            data.append(section_data)
            
        # for product in all_sections:
        #     result = dict()
            
        #     title_el = await product.query_selector('span.a-size-base-plus')
        #     result['title'] = await title_el.inner_text()
            
        #     price_el = await product.query_selector('span.a-price')
        #     result['price'] = await price_el.inner_text()
            
        #     rating_el = await product.query_selector('span.a-icon-alt')
        #     result['rating'] = await rating_el.inner_text()

        #     data.append(result)
        
        with open("results.json", "w") as file:
            json.dump(data, file, indent=4)
            
        await browser.close()
        
        
if __name__ == '__main__':
    asyncio.run(main())