numbers = list(range(1, 11))

odd_numbers = []

for number in numbers:
    if number % 2 != 0:
        odd_numbers.append(number)

print("კენტი რიცხვები:", odd_numbers)