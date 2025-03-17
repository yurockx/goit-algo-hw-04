import pathlib
import os

def get_cats_info(path):
    file_path = pathlib.Path(path)
    # checking the_file integrity_and_availability
    if not file_path.exists():
        return f"Error: File '{file_path}' does not exist or the path is wrong."
    if not file_path.is_file():
        return f"Error: '{file_path}' is not a file."
    if not os.access(file_path, os.R_OK):
        return f"Error: File '{file_path}' is not readable."
    if file_path.stat().st_size == 0:
        return f"Error: File '{file_path}' File is empty."

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.read().splitlines()
            list_cats_dics = []
            for line in lines:
                parts = line.split(',')
                dict = {}
                id = parts[0]
                name = parts[1]
                age = parts[2]
                dict.update({"id": id, "name": name, "age": age})
                list_cats_dics.append(dict)

            return list_cats_dics

    except UnicodeDecodeError:
        return "Unicode error - the file is not valid"
    except ValueError:
        print(f"Error: Invalid file path format: '{file_path}'")
    except IndexError:
        return f"Error: Index is out of range for the list. Please check the file {file_path} contains all necessary details."
    except Exception as e:  # Catch other potential errors
        return f"An unexpected error occurred: {e}"

cats_info = get_cats_info("/Users/yurii/PycharmProjects/goit-algo-hw-04/Second_task/cats.txt")
print(cats_info)
