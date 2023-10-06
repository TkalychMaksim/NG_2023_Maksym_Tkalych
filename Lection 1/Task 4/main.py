import math
while True:
    print("Choose the operation from list:\n[1] Plus\n[2] Minus\n[3] Multiply\n[4] Division\n[5] Root from number\n"
          "[6] Exponentiation ")
    user_operation = input("Chosen operation: ")
    first_number, second_number = (input("Enter 2 numbers separated by space: ").split())
    first_number = int(first_number)
    second_number = int(second_number)
    match user_operation:
        case "1" | "Plus":
            result = first_number + second_number
        case "2" | "Minus":
            result = first_number - second_number
        case "3" | "Multiply":
            result = first_number * second_number
        case "4" | "Division":
            result = first_number / second_number
        case "5" | "Root from number":
            result = math.pow(first_number, 1/second_number)
        case "6" | "Exponentiation":
            result = math.pow(first_number, second_number)
    print(result)

