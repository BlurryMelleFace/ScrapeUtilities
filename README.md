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
  - Can be added to the Windows **context menu** for quick access.

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

Make sure to close and re-open the terminal after each installation

1. Install Python 3.13
   ```bash
   winget install -e --id Python.Python.3.13
   ```
   
   Check Versions
   
   ```bash
   dir $Env:USERPROFILE\AppData\Local\Programs\Python\
   ```
   ```bash
   dir $Env:USERPROFILE\AppData\Roaming\Python\
   ```
3. Install Pipx
   ```bash
   python -m pip install --user pipx
   ```
   ```bash
   python -m pipx ensurepath
   ```
4. Install Poetry for dependency management:
   ```bash
   pipx install poetry
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

## **3. Adding `scrapeDirectory.py` to the Windows Context Menu**
You can add `scrapeDirectory.py` to the Windows **right-click context menu** for quick access to directory scraping.

### **Adding the script to the context menu**
Run the following command in an **Administrator** command prompt:
```sh
python scrapeDirectory.py add
```
This will add a **"Run My App"** option when you right-click on any folder.

### **Removing the script from the context menu**
If you wish to remove the context menu entry, run:
```sh
python scrapeDirectory.py remove
```

---

## **License**
This project is licensed under the MIT License.
