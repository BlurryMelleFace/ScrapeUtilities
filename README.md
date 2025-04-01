# ScrapeUtilities

ScrapeUtilities is a toolkit designed to streamline web scraping tasks and directory content extraction. It offers an intuitive interface for scraping images from webpages or collecting text-based file contents from a directory structure. This is particularly useful for Generative AI dataset preparation and general automation workflows.

---

## Features

### 🗂️ `scrapeDirectory.py`
Scrapes text-based file contents from a selected directory and organizes the results into structured `.txt` files.

**Highlights:**
- Select a folder via a pop-up dialog.
- Combines and saves readable file contents (`.txt`, `.py`, `.md`, `.json`, etc.) in parts of up to 10MB each.
- Skips large files and system folders like `.venv`, `node_modules`.
- Can be added to the Windows right-click context menu for instant access.

### 🌐 `scrapeImagesFromWebpage.py`
Downloads all images from one or more provided URLs and saves them into domain-specific folders.

**Highlights:**
- GUI for URL input (supports multiple URLs).
- Handles relative image paths and query strings.
- Downloads are organized into folders named after the source domain (e.g., `Scraped/google.com/`).

---

## Installation & Setup

### 1. Prerequisites
Ensure Python 3.13+ is installed and available in your system path.

```powershell
winget install -e --id Python.Python.3.13
```

Verify installed versions:

```powershell
dir $Env:USERPROFILE\AppData\Local\Programs\Python\
```

### 2. Install Pipx and Poetry
```powershell
python -m pip install --user pipx
python -m pipx ensurepath
pipx install poetry
```

### 3. Clone and Setup Repository
```bash
git clone https://github.com/your-username/ScrapeUtilities.git
cd ScrapeUtilities
poetry install
```

---

## Usage

### Run `scrapeDirectory.py`

```bash
poetry run python scrapeDirectory.py
```

- A pop-up window lets you select a directory.
- Scraped content is saved under:  
  `~/ScrapeUtility/ScrapedDirectories/<folder-name>/`

To add/remove this script to the Windows right-click menu:

```bash
# Add context menu entry
python scrapeDirectory.py add

# Remove context menu entry
python scrapeDirectory.py remove
```

---

### Run `scrapeImagesFromWebpage.py`

```bash
poetry run python scrapeImagesFromWebpage.py
```

- Paste URLs (one per line) into the popup.
- Images will be downloaded to the `Scraped/<domain>` folder.

---

## Folder Structure

```
ScrapeUtilities/
├── scrapeDirectory.py
├── scrapeImagesFromWebpage.py
├── README.md
├── pyproject.toml
├── .gitignore
└── Scraped/
    └── [output folders]
```

---

## Development

- Linting: `pylint`
- Formatting: `black`
- Testing: `pytest`

All development tools are managed via Poetry and specified under `pyproject.toml`.

---

## License

This project is licensed under the MIT License.