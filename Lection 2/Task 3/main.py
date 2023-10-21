interval_end_number = int(input("Enter the last number of interval: "))
numbers_dict = {}
first_number = 1
prime_numbers = [1]
while first_number < interval_end_number+1:
    numbers_dict[first_number] = []
    first_number += 1
for key in numbers_dict.keys():
    for second_number in range(1, interval_end_number+1):
        if key % second_number == 0:
            numbers_dict[key].append(second_number)
for key in numbers_dict.keys():
    print(f"{key}: {', '.join(str(number)for number in numbers_dict[key])}")
for key in numbers_dict.keys():
    if len(numbers_dict[key]) == 2:
        prime_numbers.append(key)
print(f"Prime numbers: {', '.join(str(prime_number) for prime_number in prime_numbers)}")
