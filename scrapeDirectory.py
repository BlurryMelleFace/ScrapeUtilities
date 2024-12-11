import os
from tkinter import Tk
from tkinter.filedialog import askdirectory

# Use a file explorer popup to select the directory
def select_directory():
    root = Tk()
    root.withdraw()  # Hide the main tkinter window
    directory = askdirectory(title="Select Directory to Scrape")
    root.destroy()
    return directory

# Function to read all file contents and write them to multiple files if larger than 10MB
def combine_file_contents(dir_path, output_folder):
    valid_extensions = ['.txt', '.py', '.md', '.yml', '.toml', '.md', '.json','.yaml']
    max_file_size = 10 * 1024 * 1024  # Maximum file size in bytes (10MB)
    file_counter = 1
    current_file_size = 0
    os.makedirs(output_folder, exist_ok=True)  # Ensure output folder exists

    # Include the output folder name in the file name for the first file
    current_output_file = os.path.join(output_folder, f"{os.path.basename(output_folder)}_part{file_counter}.txt")

    try:
        outfile = open(current_output_file, 'w', encoding='utf-8')
    except Exception as e:
        print(f"Error creating output file {current_output_file}: {e}")
        return

    for root, dirs, files in os.walk(dir_path):
        if '.venv' in dirs:
            dirs.remove('.venv')
        for file_name in files:
            file_path = os.path.join(root, file_name)
            _, file_extension = os.path.splitext(file_name)
            if file_extension in valid_extensions:
                try:
                    with open(file_path, 'r', encoding='utf-8') as infile:
                        content = f"\n\n--- Contents of {file_path} ---\n\n" + infile.read() + "\n"
                        content_size = len(content.encode('utf-8'))

                        if current_file_size + content_size > max_file_size:
                            outfile.close()
                            file_counter += 1
                            # Include the output folder name in subsequent file names
                            current_output_file = os.path.join(
                                output_folder, 
                                f"{os.path.basename(output_folder)}_part{file_counter}.txt"
                            )
                            outfile = open(current_output_file, 'w', encoding='utf-8')
                            current_file_size = 0

                        outfile.write(content)
                        current_file_size += content_size

                except Exception as e:
                    print(f"Error reading {file_path}: {e}")

    outfile.close()

if __name__ == "__main__":
    # Get the directory where this script is located
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # Create a "Scraped" folder in the script's directory
    scraped_folder = os.path.join(script_directory, "Scraped")
    os.makedirs(scraped_folder, exist_ok=True)  # Ensure "Scraped" folder exists

    print("Please select the directory to scrape.")
    directory_path = select_directory()
    if directory_path:
        selected_folder_name = os.path.basename(directory_path.rstrip(os.sep))  # Name of the selected folder
        # Create a subfolder inside "Scraped" with the name of the selected folder
        output_folder = os.path.join(scraped_folder, selected_folder_name)
        os.makedirs(output_folder, exist_ok=True)  # Ensure output folder exists

        print(f"Selected directory: {directory_path}")
        print(f"Output will be saved in: {output_folder}")
        combine_file_contents(directory_path, output_folder)
        print(f"Directory structure written to: {output_folder}")
    else:
        print("No directory selected. Exiting.")
