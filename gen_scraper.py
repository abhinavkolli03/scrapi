from playwright.async_api import async_playwright
import asyncio
import json
import os

async def scrape_page(url, selector, document_name):
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(
            headless=False
        )
        
        page = await browser.new_page()
        await page.goto(url)
        await page.wait_for_timeout(5000)
        
        all_sections = await page.query_selector_all(selector)
        data = []
            
        for sect in all_sections:
            
            section_data = {}
            checking_tags = ['h1', 'h2', 'code', 'p']
            
            for tag_name in checking_tags:
                tags = await sect.query_selector_all(tag_name)
                for i, tag in enumerate(tags, start=1):
                    text = await tag.inner_text()
                    if text.strip():
                        section_data[f"{tag_name} {i}"] = text
                    
            data.append(section_data)
        
        if not os.path.exists("scraping_results"):
            os.makedirs("scraping_results")
        
        output_file = os.path.join("scraping_results", f"{document_name}_scraperes.json")
        with open(output_file, "w") as file:
            json.dump(data, file, indent=4)
            
        await browser.close()

if __name__ == '__main__':
    doc_url = 'https://stripe.com/docs/api/errors'
    doc_selector = 'section[id^="api-section"]'
    document_name = 'stripe'
    
    asyncio.run(scrape_page(doc_url, doc_selector, document_name))
