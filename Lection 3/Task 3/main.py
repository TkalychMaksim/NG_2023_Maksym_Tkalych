import json
user_file = input("Enter the name of file: ")
target = input("Enter the key to find value in data: ")
file_name = f"{user_file}.json"
with open(file_name, 'r') as file:
    dictionary = json.load(file)


def find_target(dictionary):
    for key, value in dictionary.items():
        if key == target:
            print(f"Search value: {dictionary[key]}")
        else:
            if isinstance(value, dict):
                find_target(value)


find_target(dictionary)
