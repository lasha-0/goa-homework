def addition(a, b):
    print(f"ჯამი: {a} + {b} = {a + b}")

def subtraction(a, b):
    print(f"გამოკლება: {a} - {b} = {a - b}")

def multiplication(a, b):
    print(f"გამრავლება: {a} * {b} = {a * b}")

def division(a, b):
    if b != 0:
        print(f"გაყოფა: {a} / {b} = {a / b}")
    else:
        print("არ შეიძლება გაყოფა 0-ით!")

a = 10
b = 5

addition(a, b)
subtraction(a, b)
multiplication(a, b)
division(a, b)





