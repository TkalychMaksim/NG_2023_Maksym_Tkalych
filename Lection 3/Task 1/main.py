input_filename = input("Enter the filename with '.txt' end: ")
letters_vocabulary = {}
symbols_vocabulary = {}
alphabet = 'abcdefghijklmnopqrstuvwxyz'
try:
    with open(input_filename, 'r') as f:
        for line in f.readlines():
            for symbol in line:
                if symbol in alphabet:
                    if symbol in letters_vocabulary:
                        letters_vocabulary[symbol] += 1
                    else:
                        letters_vocabulary[symbol] = 1
                else:
                    if symbol in symbols_vocabulary:
                        symbols_vocabulary[symbol] += 1
                    else:
                        symbols_vocabulary[symbol] = 1
    print(f"Letters: {letters_vocabulary}")
    print(f"Symbols: {symbols_vocabulary}")

except IOError as e:
    print("Error opening file")



