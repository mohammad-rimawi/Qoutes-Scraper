# Quotes to Scrape Scraper

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Playwright](https://img.shields.io/badge/Playwright-Installed-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

**Quotes to Scrape Scraper** is a Python tool that uses [Playwright](https://playwright.dev/python/docs/intro) to scrape quotes, authors, and tags from [Quotes to Scrape](https://quotes.toscrape.com/).

---

## Features

- Scrape quotes, their authors, and associated tags.
- Export data to JSON (`data/quotes.json`) or CSV (`data/quotes.csv`).
- Use command-line arguments to choose the output format.
- Works on Windows, Linux, and MacOS.

---

## Requirements

- Python 3.9 or higher
- Required Python packages:
```bash
pip install playwright pandas
playwright install
