user_input_temperature = float(input("Enter the temperature: "))
print("Select the conversion method\n[1] Celsius->Fahrenheit\n[2] Fahrenheit->Celsius")
user_system_choice = input("Chosen method: ")
if user_system_choice == "1":
    print(f"{user_input_temperature} C -> {((user_input_temperature*9)/5) + 32} F")
elif user_system_choice == "2":
    print(f"{user_input_temperature} F -> {((user_input_temperature-32) *(5/9))} C")
else:
    print("Method Error")