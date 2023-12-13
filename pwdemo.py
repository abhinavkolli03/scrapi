import json
from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        page.goto("https://playwright.dev/")

        title = page.title()
        print(f"Page Title: {title}")

        get_started_link = page.get_by_role("link", name="Get started")
        if get_started_link:
            get_started_link.click()
            installation_heading = page.get_by_role("heading", name="Installation").is_visible()
            print(f"Installation Heading Visible: {installation_heading}")

        results = {
            "title": title,
            "installation_heading_visible": installation_heading if "installation_heading" in locals() else None
        }

        with open("results.json", "w") as json_file:
            json.dump(results, json_file)

        browser.close()

if __name__ == "__main__":
    main()
