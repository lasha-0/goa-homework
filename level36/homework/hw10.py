def print_even_numbers(n):
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(i)

n = int(input("შეიყვანეთ რიცხვი: "))
print_even_numbers(n)