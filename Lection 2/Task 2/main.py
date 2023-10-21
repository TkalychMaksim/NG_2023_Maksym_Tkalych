user_list = input("Enter your elements separated by space: ").split()
number_counter = 0
print("Numbers list: ")
for element in user_list:
    if element.isdigit():
        print(element)
        number_counter += 1
print("The count of numbers: " + str(number_counter))


