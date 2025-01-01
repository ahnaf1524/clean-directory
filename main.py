# Only for windows machine
import os
import shutil
import colorama
from colorama import Fore, Style

def remove_unwanted_files(folder_path):
    try:
        # Check if folder path exists
        if not os.path.exists(folder_path):
            print(Fore.RED + "Error: The provided folder path does not exist." + Style.RESET_ALL)
            return

        # Initialize counters
        removed_files = 0
        removed_folders = 0

        # Remove specific folders
        for folder_name in ['.vscode', '.cph']:
            folder_to_remove = os.path.join(folder_path, folder_name)
            if os.path.exists(folder_to_remove):
                shutil.rmtree(folder_to_remove)
                print(Fore.YELLOW + f"Removed folder: {folder_to_remove}" + Style.RESET_ALL)
                removed_folders += 1

        # Remove specific files
        for root, _, files in os.walk(folder_path):
            for file_name in files:
                # Match unwanted files
                if file_name in ['tempCodeRunnerFile.c', 'tempCodeRunnerFile.cpp' , 'input.txt' , 'input.in' , 'output.txt' , 'output.out'] or file_name.endswith('.exe'):
                    file_to_remove = os.path.join(root, file_name)
                    os.remove(file_to_remove)
                    print(Fore.YELLOW + f"Removed file: {file_to_remove}" + Style.RESET_ALL)
                    removed_files += 1

        # Success message
        print(Fore.GREEN + "\nOperation Success!" + Style.RESET_ALL)
        print(Fore.CYAN + f"Summary: {removed_files} files and {removed_folders} folders removed." + Style.RESET_ALL)

    except Exception as e:
        print(Fore.RED + f"An error occurred: {e}" + Style.RESET_ALL)

if __name__ == "__main__":
    colorama.init(autoreset=True)
    folder_path = input("Enter the Windows folder path: ").strip()
    remove_unwanted_files(folder_path)
