from colorama import Fore

def note_c_folder(message):
    print(f"{Fore.BLUE} {message} {Fore.RESET}")

def note_c_file(message):
    print(f"{Fore.YELLOW} {message} {Fore.RESET}")

# def note_c_error(message):
#     print(f"{Fore.RED} [ERROR] {Fore.RESET} {message}")