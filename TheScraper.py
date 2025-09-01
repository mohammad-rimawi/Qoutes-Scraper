from playwright.sync_api import sync_playwright
from dataclasses import dataclass, asdict
import argparse
import pandas as pd
import json
import os


@dataclass
class Quotes:
    quote: str = None
    author: str = None
    tags: list = None

def scrape_quotes():
    all_quotes = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True) 
        page = browser.new_page()
        page.goto("https://quotes.toscrape.com/", timeout=30000)
        page.wait_for_timeout(2000)

        # Get all quote blocks
        quote_blocks = page.locator('//div[@class="quote"]')
        count = quote_blocks.count()

        for i in range(count):
            quote_element = quote_blocks.nth(i)
            quote_text = quote_element.locator('span.text').inner_text()
            author = quote_element.locator('small.author').inner_text()
            tags = quote_element.locator('a.tag').all_inner_texts()

            q = Quotes(quote=quote_text, author=author, tags=tags)
            all_quotes.append(asdict(q))

        browser.close()
    return all_quotes

def save_data(data, file_format):
    os.makedirs("data", exist_ok=True)

    if file_format == "json":
        with open("data/quotes.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(" Data saved to data/quotes.json")

    elif file_format == "csv":
        df = pd.DataFrame(data)
        df.to_csv("data/quotes.csv", index=False, encoding="utf-8-sig")
        print(" Data saved to data/quotes.csv")

def main():
    parser = argparse.ArgumentParser(description="Quotes Scraper using Playwright")
    parser.add_argument("--format", choices=["json", "csv"], default="json", help="Choose output format")
    args = parser.parse_args()

    print(" Scraping in progress...")
    data = scrape_quotes()
    save_data(data, args.format)

if __name__ == "__main__":
    main()


        





