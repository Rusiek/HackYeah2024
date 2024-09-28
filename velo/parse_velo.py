import ast

def parse_txt_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read().strip()

    # Use ast.literal_eval for safe evaluation
    data = ast.literal_eval(content)

    return data

# Usage
file_path = 'D:\\DEV\\GIT\\HackYeah2024\\velo\\velo.txt'  # Replace with your actual file path
parsed_data = parse_txt_file(file_path)

# Printing the parsed data
for array in parsed_data:
    print(array)
    for tuple_element in array:
        print(tuple_element)