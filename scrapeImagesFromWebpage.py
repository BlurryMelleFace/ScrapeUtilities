import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import tkinter as tk
from tkinter import messagebox


def get_domain_name(url):
    """
    Extracts the domain name from a URL.
    
    Args:
        url (str): The URL to extract the domain name from.
    
    Returns:
        str: The domain name (e.g., "google.de").
    """
    parsed_url = urlparse(url)
    domain = parsed_url.netloc  # Extracts "www.google.de"
    if domain.startswith("www."):
        domain = domain[4:]  # Remove "www."
    return domain


def download_images_from_url(url, output_folder):
    """
    Downloads all images from a given URL and saves them into an organized folder.

    Args:
        url (str): The webpage URL to scrape images from.
        output_folder (str): The path to the folder where images will be saved.

    Returns:
        None
    """
    try:
        # Fetch the HTML content of the URL
        response = requests.get(url)
        response.raise_for_status()
        
        # Parse HTML content with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all image tags
        img_tags = soup.find_all('img')
        if not img_tags:
            print(f"No images found on {url}")
            return
        
        # Ensure the output folder exists
        os.makedirs(output_folder, exist_ok=True)
        
        # Download each image
        for img_tag in img_tags:
            img_url = img_tag.get('src')
            if not img_url:
                continue
            
            # Handle relative URLs
            img_url = urljoin(url, img_url)
            
            # Get the image filename
            img_name = os.path.basename(img_url.split("?")[0])  # Remove query params
            
            # Download the image
            try:
                img_data = requests.get(img_url).content
                with open(os.path.join(output_folder, img_name), 'wb') as img_file:
                    img_file.write(img_data)
                print(f"Downloaded: {img_name}")
            except Exception as e:
                print(f"Failed to download {img_url}: {e}")
        
    except Exception as e:
        print(f"Error processing {url}: {e}")


def scrape_images(urls, base_output_folder='Scraped'):
    """
    Scrapes images from a list of URLs and organizes them into separate folders.

    Args:
        urls (list): List of webpage URLs to scrape images from.
        base_output_folder (str): Base folder to store all scraped images.

    Returns:
        None
    """
    for url in urls:
        domain_name = get_domain_name(url)
        output_folder = os.path.join(base_output_folder, domain_name)
        print(f"Scraping images from: {url}")
        download_images_from_url(url, output_folder)
    messagebox.showinfo("Success", "Image scraping completed!")


def open_popup():
    """
    Opens a popup window to input multiple URLs for scraping.
    """
    def start_scraping():
        urls = text_box.get("1.0", tk.END).strip().split("\n")
        urls = [url.strip() for url in urls if url.strip()]
        if not urls:
            messagebox.showerror("Error", "No URLs provided!")
            return
        scrape_images(urls)

    # Create a popup window
    popup = tk.Tk()
    popup.title("Image Scraper")
    
    # Instruction label
    label = tk.Label(popup, text="Paste URLs (one per line):")
    label.pack(pady=5)
    
    # Text box for URLs
    text_box = tk.Text(popup, height=10, width=50)
    text_box.pack(pady=5)
    
    # Start button
    start_button = tk.Button(popup, text="Start Scraping", command=start_scraping)
    start_button.pack(pady=5)
    
    popup.mainloop()


if __name__ == "__main__":
    open_popup()
