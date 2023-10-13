user_letters_list = input("Enter your string: ")
vowels = 'aeiouy'
user_vowels_list = []
for letter in user_letters_list:
    if letter in vowels:
        user_vowels_list.append(letter)
print(f"Vowels: {' '.join(user_vowels_list)}")