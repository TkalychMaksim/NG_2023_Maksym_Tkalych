input_filename = input("Enter the filename with '.txt' end: ")
try:
    with open(input_filename, 'r') as file:
        text = file.read()
        for symbol in set(text):
            count = text.count(symbol)
            print(f"{symbol}: {count}")
except IOError as error:
    print("Error opening file")


