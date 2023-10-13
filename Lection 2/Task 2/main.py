user_list = input("Enter your elements separated by space: ").split()
numbers_list = []
for element in user_list:
    if element.isdigit():
        numbers_list.append(element)
print(f"Count of numbers in your string: {len(numbers_list)}\n{', '.join(str(number)for number in numbers_list)}")

