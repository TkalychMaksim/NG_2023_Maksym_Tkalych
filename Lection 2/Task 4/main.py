user_letters_list = input("Enter your string: ")
vowels = 'aeiouy'
for letter in user_letters_list:
    if letter in vowels:
        print(letter, end=' ')
