interval_end_number = int(input("Enter the last number of interval: "))
numbers_dict = {}
first_number = 1
prime_numbers = [1]
for number in range(1, interval_end_number+1):
    numbers_dict[number] = []
    divisors = [divisor for divisor in range(1, number+1) if number % divisor == 0]
    numbers_dict[number] = divisors
    print(f"{number}: {', '.join(str(divisor) for divisor in numbers_dict[number])}")
for key in numbers_dict.keys():
    if len(numbers_dict[key]) == 2:
        prime_numbers.append(key)
print(f"Prime numbers: {', '.join(str(prime_number) for prime_number in prime_numbers)}")
