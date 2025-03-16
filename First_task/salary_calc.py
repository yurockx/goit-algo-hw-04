import pathlib
import os

# Function to calculate total and average amount of salary from the file
def total_salary(filepath):
    path = pathlib.Path(filepath)
    #checking the_file integrity_and_availability
    if not path.exists():
        return f"Error: File '{path}' does not exist."
    if not path.is_file():
        return f"Error: '{path}' is not a file."
    if not os.access(path, os.R_OK):
        return f"Error: File '{path}' is not readable."
    if path.stat().st_size == 0:
        return f"Error: File '{path}' File is empty."

    try:
        with open(path, "r", encoding="utf-8") as file:
            lines = file.read().splitlines()
            salaries = []
            for line in lines:
                parts = line.split(',')
                for part in parts:
                    if part.isdigit():
                        salaries.append(int(part))
            if not salaries:
                return f"Error: the file {path} doesn't contain salary numbers."

            total_salary = sum(salaries)
            average_salary = total_salary // len(salaries)  # Integer division
            return total_salary, average_salary

    except UnicodeDecodeError:
        return "Unicode error - the file is not valid"
    except ValueError:
        print(f"Error: Invalid file path format: '{path}'")
    except Exception as e:
        return f"Unknown error occurred: {e}."

#TEST
# result = total_salary("/Users/yurii/PycharmProjects/goit-algo-hw-04/First_task/employees_list.txt")
#
# if isinstance(result, str):
#     print(result)  # Print the error message
# else:
#     total, average = result
#     print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
