
# **ScrapeUtilities**

This repository provides tools and scripts to simplify the process of scraping and organizing scraped content. Designed for users dealing with repetitive data extraction tasks, such as those for **Generative AI applications**.

---

## **Contents**
- **[`scrapeDirectory.py`](scrapeDirectory.py):**  
  A Python script that allows users to scrape the contents of a directory and organize it into structured files. It dynamically creates folders for scraped content, making it reusable and easy to manage.  
  **Key Features:**
  - Allows the user to select a directory to scrape using a pop-up window.
  - Organizes scraped content into a `Scraped` folder.
  - Automatically excludes dynamic content from version control using `.gitignore`.

- **[`scrapeImagesFromWebpage.py`](scrapeImagesFromWebpage.py):**  
  A Python script that downloads all images from one or more provided URLs and organizes them into structured folders.  
  **Key Features:**
  - Accepts multiple URLs through a user-friendly pop-up window.
  - Downloads images into `Scraped/Website_<n>` directories.
  - Handles relative URLs and query parameters seamlessly.

- **[`.gitignore`](.gitignore):**  
  Ensures that the contents of the `Scraped` folder are not tracked by Git while keeping the folder structure in the repository.

- **[`README.md`](README.md):**  
  Documentation for the repository, providing details on how to use the utilities.

---

## **Setup Instructions**

### **1. Prerequisites**
1. Install Python 3.9+.
2. Install Poetry for dependency management:
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

### **2. Clone the Repository**
   ```bash
   git clone https://github.com/your-username/ScrapeUtilities.git
   cd ScrapeUtilities
   ```

### **3. Install Dependencies**
   Run the following command to install all dependencies in an isolated environment:
   ```bash
   poetry install
   ```

---

## **Usage**

### **1. Using `scrapeDirectory.py`**
   - Open the terminal in the repository directory.
   - Run the script:
     ```bash
     poetry run python scrapeDirectory.py
     ```
   - A pop-up window will allow you to select the directory you wish to scrape.
   - The scraped files will be saved in a `Scraped/<selected-folder-name>` directory, dynamically created within the repository.

### **2. Using `scrapeImagesFromWebpage.py`**
   - Open the terminal in the repository directory.
   - Run the script:
     ```bash
     poetry run python scrapeImagesFromWebpage.py
     ```
   - A pop-up window will allow you to paste multiple URLs (one per line).
   - Images will be downloaded into structured subdirectories inside the `Scraped/` folder (e.g., `Scraped/Website_1`, `Scraped/Website_2`).

---

## **Development**

To work within the Poetry virtual environment:
1. Activate the environment:
   ```bash
   poetry shell
   ```
2. Run your scripts directly:
   ```bash
   python scrapeDirectory.py
   ```
3. Exit the environment when done:
   ```bash
   exit
   ```

---

## **License**
This project is licensed under the MIT License.
