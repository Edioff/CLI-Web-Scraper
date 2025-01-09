# CLI Web Scraper

Este proyecto es una aplicación CLI para extraer detalles de propiedades en venta desde el sitio [RealityRealtyPR](https://www.realityrealtypr.com/). Permite obtener información sobre casas y apartamentos de una página específica y guardarla en un archivo JSON.

## 📌 Instalación

### 1. Clonar el repositorio

```
git clone https://github.com/Edioff/CLI-Web-Scraper.git
cd CLI-Web-Scraper
```

### 2. Instalar las dependencias con Poetry

```
poetry install
```

### 3. Instalar los navegadores para Playwright

```
poetry run playwright install --with-deps
```

## 🚀 Uso

Para ejecutar el scraper, usa el siguiente comando:

```
poetry run python scraper.py <HOUSE | APARTMENT> <page_number> <output_file>
```

### Ejemplo

Extraer la primera página de casas y guardarla en `casas.json`:

```
poetry run python scraper.py HOUSE 0 casas.json
```

## 📂 Formato de salida (`output_file`)

El archivo JSON generado tendrá la siguiente estructura:

```
[
  {
    "url": "https://www.realityrealtypr.com/compra-venta/casa/puerto-rico/cayey/bo-toita/166209",
    "title": "Bo. Toita",
    "city": "Cayey",
    "price": "Venta: $140,000",
    "description": "Propiedad de 2 niveles con 4 habitaciones...",
    "images": [
      "https://s3.amazonaws.com/app-propiedades/166209/1_large.jpg",
      "https://s3.amazonaws.com/app-propiedades/166209/2_large.jpg"
    ],
    "flyer": "https://www.realityrealtypr.com/properties/print/id:166209/broker_id:14011/"
  }
]
```

## 📁 Estructura del Proyecto

```
CLI-Web-Scraper/
│── scraper.py        # Script principal del scraper
│── pyproject.toml    # Archivo de configuración de Poetry
│── README.md         # Documentación del proyecto
```

## 📦 Dependencias

Las dependencias utilizadas en este proyecto están definidas en `pyproject.toml` e incluyen:

- `playwright`: Para automatización web.
- `requests`: Para manejo de peticiones HTTP.
- `beautifulsoup4` y `lxml`: Para parsing de HTML.
- `rich`: Para mejorar la visualización en consola.

## ⚠ Notas

- Se recomienda ejecutar `poetry run playwright install --with-deps` si es la primera vez que se usa Playwright.
- El script solo obtiene las propiedades de la página especificada en el argumento y no navega por todas las páginas.
- Si experimentas problemas con dependencias, puedes ejecutar `poetry update` para asegurarte de tener las versiones correctas.

## 📜 Licencia

Este proyecto no tiene una licencia definida.
