import sys
import pathlib
from colorama import Fore, init

init(autoreset=True)  #reset colors after each print

#Recursively displays folder and subfolders items

# Args
#path (str): The path to the folder to display.
#         indent (str, optional): The indentation string for visual hierarchy.

def subitems(path: str, indent: str = ""):
     current_path = pathlib.Path(path)

     if not current_path.exists():
         print(f"{Fore.RED}Error: '{path}' does not exist.")
         return
     if not current_path.is_dir():
         print(f"{Fore.RED}Error: '{path}' is not a valid directory.")
         return

     try:
         items = sorted(current_path.iterdir())
         for item in items:
             if item.is_dir():
                 print(indent + f"{Fore.BLUE} {item.name}/")
                 subitems(item, indent + "│  ")  # | -> line to see subfolders level
             else:
                 print(indent + f"{Fore.YELLOW} {item.name}")

         if not current_path.is_dir():
             print(f"Error: '{current_path}' is not a valid directory.")
     except OSError as e:
         print(f"{Fore.RED}Error accessing '{path}': {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        subitems(sys.argv[1])
    else:
        print("Use correct command: python subitems.py <directory/path> ->with no spaces otherwise add quotes")
