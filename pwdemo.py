import json
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

def extract_api_information(page):
    # Extract information from different sections of the page
    api_intro = page.inner_html('section:has-text("API Reference")')
    authentication = page.inner_html('section:has-text("Authentication")')
    authenticated_request = page.inner_html('section:has-text("AUTHENTICATED REQUEST")')
    errors = page.inner_html('section:has-text("Errors")')
    print("hello")

    # Create labeled JSON objects for each section
    api_info = {
        "API Reference": api_intro,
        "Authentication": authentication,
        "Authenticated Request": authenticated_request,
        "Errors": errors
    }

    return api_info

def extract_meaningful_text(api_info):
    soup = BeautifulSoup(api_info, 'html.parser', from_encoding='utf-8')
    meaningful_data = soup.find('div').get_text()
    return meaningful_data

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        page.goto("https://stripe.com/docs/api", timeout=100000)
        
        # Extract API information
        api_info = extract_api_information(page)
        
        meaningful_data = extract_meaningful_text(api_info)
        
        print(meaningful_data)

        browser.close()

if __name__ == "__main__":
    main()
