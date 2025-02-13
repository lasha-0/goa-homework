import random
numbers = [random.randint(1, 100) for _ in range(10)]

total_sum = 0
for number in numbers:
    total_sum += number

print(numbers)
print(total_sum)