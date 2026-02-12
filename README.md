# CLI Web Scraper — Puerto Rico Real Estate

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-2EAD33?style=flat-square&logo=playwright&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

> Command-line tool for extracting property listings from Puerto Rican real estate portals. Built with Playwright and BeautifulSoup for reliable data extraction.

## Overview

Scrapes property listings (houses and apartments) from [Reality Realty PR](https://www.realityrealtypr.com/), extracting detailed property information and saving it as structured JSON. Designed as a CLI tool with configurable parameters for property type, pagination, and output.

## Features

- **CLI interface** — Simple command-line usage with configurable parameters
- **Property types** — Houses and apartments
- **Structured output** — Clean JSON with URL, title, city, price, description, images
- **Playwright rendering** — Handles JavaScript-rendered content
- **Flyer generation** — Includes links to property flyers

## Output Format

```json
[
  {
    "url": "https://www.realityrealtypr.com/compra-venta/casa/puerto-rico/cayey/...",
    "title": "Bo. Toita",
    "city": "Cayey",
    "price": "Venta: $140,000",
    "description": "Propiedad de 2 niveles con 4 habitaciones...",
    "images": [
      "https://s3.amazonaws.com/app-propiedades/166209/1_large.jpg"
    ],
    "flyer": "https://www.realityrealtypr.com/properties/print/id:166209/"
  }
]
```

## Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-2EAD33?style=flat-square&logo=playwright&logoColor=white)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-lxml-orange?style=flat-square)

- **Playwright** — Browser automation for JS-rendered pages
- **BeautifulSoup + lxml** — HTML parsing
- **Rich** — Terminal UI formatting
- **Poetry** — Dependency management

## Installation

```bash
git clone https://github.com/Edioff/CLI-Web-Scraper.git
cd CLI-Web-Scraper
poetry install
poetry run playwright install --with-deps
```

## Usage

```bash
poetry run python scraper.py <HOUSE|APARTMENT> <page_number> <output_file>
```

### Examples

```bash
# Scrape first page of houses
poetry run python scraper.py HOUSE 0 houses.json

# Scrape apartments page 3
poetry run python scraper.py APARTMENT 3 apartments.json
```

## Notes

- Designed for educational purposes
- Scrapes one page per execution
- Respect the target site's Terms of Service

## Author

**Johan Cruz** — Data Engineer & Web Scraping Specialist
- GitHub: [@Edioff](https://github.com/Edioff)
- Available for freelance projects

## License

MIT
