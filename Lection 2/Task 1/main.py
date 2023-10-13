user_list = (input("Enter your elements separated by space: ")).split()
unique_user_list = set(user_list)
print(f"Unique elements: {', '.join(str(element) for element in unique_user_list)}")

