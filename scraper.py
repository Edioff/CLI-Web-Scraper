import json
import sys
from playwright.sync_api import sync_playwright
from collections import OrderedDict

# Base URL del sitio web
BASE_URL = "https://www.realityrealtypr.com"

# Mapeo de tipos de propiedad
PROPERTY_TYPES = {"HOUSE": "Residential%3A1", "APARTMENT": "Residential%3A5"}

def build_url(property_type, page_number):
    """Construye la URL con los filtros correctos para el scraping."""
    return f"{BASE_URL}/properties/type:venta/pagination:size%7C15%7Cpage%7C{page_number}/?search%5Bproperty_type%5D={PROPERTY_TYPES[property_type]}"

def get_text_or_default(page, selector, default="N/A"):
    """Obtiene el texto de un elemento o devuelve un valor por defecto si no se encuentra."""
    try:
        return page.locator(selector).inner_text()
    except:
        return default

def get_attribute_or_default(page, selector, attribute, default="N/A"):
    """Obtiene un atributo de un elemento o devuelve un valor por defecto si no se encuentra."""
    try:
        return page.locator(selector).first.get_attribute(attribute) or default
    except:
        return default

def scrape_property_details(page, link):
    """Extrae los detalles de una propiedad desde su página individual."""
    page.goto(BASE_URL + link, wait_until="load")

    return {
        "url": BASE_URL + link.split("?")[0],
        "title": get_text_or_default(page, "#top-content h1"),
        "city": get_text_or_default(page, "#top-content > div > div:nth-child(2) > div.col-xs-12.col-sm-8 > p"),
        "price": get_text_or_default(page, ".row.margin-top h3"),
        "description": get_text_or_default(page, "#home"),
        "images": [img.get_attribute("src") for img in page.locator("#thumbcarousel img").all() if img.get_attribute("src")],
        "flyer": get_attribute_or_default(page, "#top-content .title-side span a", "href")
    }

def scrape_all_properties(property_type, page_number, output_file):
    """Extrae los enlaces de propiedades y obtiene sus detalles."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(build_url(property_type, page_number), wait_until="load")

        # Obtener enlaces de todas las propiedades listadas en la página
        property_links = list(OrderedDict.fromkeys([
            el.get_attribute("href") for el in page.locator(".results .result h3 a").all()
        ]))

        print(f"📌 Procesando {len(property_links)} propiedades en la página {page_number}...")

        # Extraer detalles de cada propiedad
        properties_data = []
        for link in property_links:
            print(f"🔍 Scraping {BASE_URL + link} ...")
            try:
                properties_data.append(scrape_property_details(page, link))
            except Exception as e:
                print(f"⚠️ Error en {BASE_URL + link}: {e}")

        # Guardar datos en el archivo JSON
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(properties_data, f, indent=4, ensure_ascii=False)

        print(f"\n✅ Datos guardados en {output_file}")
        browser.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Uso: python3 scraper.py <HOUSE | APARTMENT> <page_number> <output_file>")
        sys.exit(1)

    scrape_all_properties(sys.argv[1].upper(), sys.argv[2], sys.argv[3])
