import os
import sys
import winreg as reg
from tkinter import Tk
from tkinter.filedialog import askdirectory
import os
import subprocess

# Function to select a directory with Tkinter (fallback if no argument is passed)
def select_directory():
    root = Tk()
    root.withdraw()
    directory = askdirectory(title="Select Directory to Scrape")
    root.destroy()
    return directory

# Function to combine and write file contents to output files
def combine_file_contents(dir_path, output_folder):
    valid_extensions = ['.txt', '.py', '.md', '.yml', '.toml', '.json', '.yaml']
    max_file_size = 10 * 1024 * 1024  # 10MB
    file_counter = 1
    current_file_size = 0

    os.makedirs(output_folder, exist_ok=True)
    current_output_file = os.path.join(output_folder, f"{os.path.basename(output_folder)}_part{file_counter}.txt")

    outfile = open(current_output_file, 'w', encoding='utf-8')

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
                            current_output_file = os.path.join(output_folder, f"{os.path.basename(output_folder)}_part{file_counter}.txt")
                            outfile = open(current_output_file, 'w', encoding='utf-8')
                            current_file_size = 0

                        outfile.write(content)
                        current_file_size += content_size
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")

    outfile.close()

# Add context menu entry
def add_to_context_menu():
    # Dynamically determine the correct path
    if getattr(sys, 'frozen', False):  # Packaged with PyInstaller
        app_path = sys.executable
    else:
        app_path = os.path.abspath(__file__)

    reg_path = r"Directory\shell\RunMyApp"
    command_path = rf"{reg_path}\command"

    try:
        with reg.CreateKey(reg.HKEY_CLASSES_ROOT, reg_path) as key:
            reg.SetValue(key, '', reg.REG_SZ, "Run My App")
        with reg.CreateKey(reg.HKEY_CLASSES_ROOT, command_path) as key:
            reg.SetValue(key, '', reg.REG_SZ, f'"{app_path}" "%1"')
        print("Context menu entry successfully added!")
    except Exception as e:
        print(f"Error adding to context menu: {e}")

def remove_from_context_menu():
    reg_path = r"Directory\shell\RunMyApp"
    try:
        # Delete the 'command' subkey first
        with reg.OpenKey(reg.HKEY_CLASSES_ROOT, reg_path + r"\command", 0, reg.KEY_WRITE) as command_key:
            reg.DeleteKey(reg.HKEY_CLASSES_ROOT, reg_path + r"\command")
            print("Deleted 'command' subkey.")

        # Delete the 'RunMyApp' key
        with reg.OpenKey(reg.HKEY_CLASSES_ROOT, reg_path, 0, reg.KEY_WRITE) as runmyapp_key:
            reg.DeleteKey(reg.HKEY_CLASSES_ROOT, reg_path)
            print("Deleted 'RunMyApp' key.")

        print("Context menu entry successfully removed!")
    except FileNotFoundError:
        print("Context menu entry not found.")
    except PermissionError:
        print("Permission denied. Please run the script as an administrator.")
    except Exception as e:
        print(f"Error removing context menu entry: {e}")

# Main execution logic
if __name__ == "__main__":
    # If the script is run via the context menu, a folder path is passed as an argument
    if len(sys.argv) > 1:
        directory_path = sys.argv[1]
    else:
        # No folder passed, use the Tkinter GUI to select one
        directory_path = select_directory()

    if directory_path:
        script_directory = os.path.dirname(os.path.abspath(__file__))
        scraped_folder = os.path.join(script_directory, "Scraped")
        os.makedirs(scraped_folder, exist_ok=True)
        selected_folder_name = os.path.basename(directory_path.rstrip(os.sep))
        output_folder = os.path.join(scraped_folder, selected_folder_name)
        os.makedirs(output_folder, exist_ok=True)
        print(f"Selected directory: {directory_path}")
        print(f"Output will be saved in: {output_folder}")
        combine_file_contents(directory_path, output_folder)
        print(f"Directory structure written to: {output_folder}")


        print(f"\nPress Enter to open the output folder. Closing the terminal will also close the folder.")
        input() 

        folder_process = subprocess.Popen(['explorer', output_folder])
        
    else:
        print("No directory selected. Exiting.")

    action = input("Type 'add' to add, 'remove' to remove the context menu entry, or press Enter to skip: ").strip().lower()
    if action == "add":
        add_to_context_menu()
    elif action == "remove":
        remove_from_context_menu()
