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

- **[`.gitignore`](.gitignore):**  
  Ensures that the contents of the `Scraped` folder are not tracked by Git while keeping the folder structure in the repository.

- **[`README.md`](README.md):**  
  Documentation for the repository, providing details on how to use the utilities.

---

## **Usage**

### **1. Set Up**
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ScrapeUtilities.git
   cd ScrapeUtilities
   ```
2. Install Python if you don’t have it already installed on your machine.

### **2. Using `scrapeDirectory.py`**
   - Open the terminal in the repository directory.
   - Run the script:
     ```bash
     python scrapeDirectory.py
     ```
   - A pop-up window will allow you to select the directory you wish to scrape.
   - The scraped files will be saved in a `Scraped/<selected-folder-name>` directory, dynamically created within the repository.
