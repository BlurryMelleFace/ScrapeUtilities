import os
import sys
import winreg as reg
from tkinter import Tk
from tkinter.filedialog import askdirectory
import subprocess


def select_directory():
    root = Tk()
    root.withdraw()
    directory = askdirectory(title="Select Directory to Scrape")
    root.destroy()
    return directory


def combine_file_contents(dir_path, output_folder):
    valid_extensions = ['.txt', '.py', '.md', '.yml', '.toml', '.json', '.yaml','.html','.js','.css','.ts','.scss']
    max_file_size = 10 * 1024 * 1024  
    file_counter = 1
    current_file_size = 0

    os.makedirs(output_folder, exist_ok=True)
    current_output_file = os.path.join(output_folder, f"{os.path.basename(output_folder)}_part{file_counter}.txt")

    outfile = open(current_output_file, 'w', encoding='utf-8')

    for root, dirs, files in os.walk(dir_path):
        if '.venv' in dirs:
            dirs.remove('.venv')
        if 'node_modules' in dirs:
            dirs.remove('node_modules')
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

def add_to_context_menu():
    app_path = sys.executable  # Path to Python executable
    script_path = os.path.abspath(__file__)  # Path to this script
    icon_path = os.path.join(os.path.dirname(script_path), "scrape_icon.ico")  # Path to the icon

    reg_path = r"Directory\shell\ScrapeThisDirectory"
    command_path = rf"{reg_path}\command"

    try:
        with reg.CreateKey(reg.HKEY_CLASSES_ROOT, reg_path) as key:
            reg.SetValue(key, '', reg.REG_SZ, "Scrape This Directory")
            reg.SetValueEx(key, "Icon", 0, reg.REG_SZ, icon_path)  # Add an icon

        with reg.CreateKey(reg.HKEY_CLASSES_ROOT, command_path) as key:
            reg.SetValue(key, '', reg.REG_SZ, f'"{app_path}" "{script_path}" "%1"')  # Explicitly run script

        print("Context menu entry successfully added!")
    except Exception as e:
        print(f"Error adding to context menu: {e}")

def remove_from_context_menu():
    reg_path = r"Directory\shell\ScrapeThisDirectory"
    try:
        with reg.OpenKey(reg.HKEY_CLASSES_ROOT, reg_path + r"\command", 0, reg.KEY_WRITE) as command_key:
            reg.DeleteKey(reg.HKEY_CLASSES_ROOT, reg_path + r"\command")
            print("Deleted 'command' subkey.")
        with reg.OpenKey(reg.HKEY_CLASSES_ROOT, reg_path, 0, reg.KEY_WRITE) as runmyapp_key:
            reg.DeleteKey(reg.HKEY_CLASSES_ROOT, reg_path)
            print("Deleted 'Scrape This Directory' key.")
        print("Context menu entry successfully removed!")
    except FileNotFoundError:
        print("Context menu entry not found.")
    except PermissionError:
        print("Permission denied. Please run the script as an administrator.")
    except Exception as e:
        print(f"Error removing context menu entry: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        action = sys.argv[1].lower()
        if action == "add":
            add_to_context_menu()
        elif action == "remove":
            remove_from_context_menu()
        elif os.path.isdir(sys.argv[1]):
            directory_path = sys.argv[1]
        else:
            print(f"Invalid argument: {sys.argv[1]}. Use 'add', 'remove', or pass a valid directory path.")
            sys.exit()
    else:
        directory_path = select_directory()

    if 'directory_path' in locals() and directory_path:
        if getattr(sys, 'frozen', False):
            script_directory = os.path.dirname(sys.executable)
        else:
            script_directory = os.path.dirname(os.path.abspath(__file__))

        output_folder = os.path.join(os.path.expanduser("~\ScrapeUtility\ScrapedDirectories"), os.path.basename(directory_path.rstrip(os.sep)))
        os.makedirs(output_folder, exist_ok=True)
        print(f"Selected directory: {directory_path}")
        print(f"Output will be saved in: {output_folder}")
        combine_file_contents(directory_path, output_folder)

        if os.path.exists(output_folder):
            print(f"\nPress Enter to open the output folder.")
            input()
            subprocess.Popen(['explorer', output_folder])
        else:
            print("Output folder does not exist.")