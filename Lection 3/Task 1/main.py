input_filename = input("Enter the filename with '.txt' end: ")
symbols_vocabulary = {}
alphabet = 'abcdefghijklmnopqrstuvwxyz'
try:
    with open(input_filename, 'r') as f:
        for symbol in f.read():
            if symbol in symbols_vocabulary:
                symbols_vocabulary[symbol] += 1
            else:
                symbols_vocabulary[symbol] = 1
except IOError as e:
    print("Error opening file")
finally:
    for symbol in symbols_vocabulary:
        print(f"{symbol}: {symbols_vocabulary[symbol]}")




