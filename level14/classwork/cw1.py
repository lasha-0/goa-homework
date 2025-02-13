number1 = float(input("გთხოვთ, შეიყვანოთ პირველი რიცხვი: "))
number2 = float(input("გთხოვთ, შეიყვანოთ მეორე რიცხვი: "))

print(f"({number1} > 5 and {number2} > 5): {number1 > 5 and number2 > 5}")
print(f"({number1} < 10 and {number2} < 10): {number1 < 10 and number2 < 10}") 
print(f"({number1} == {number2} and {number1} > 0): {number1 == number2 and number1 > 0}")

print(f"({number1} > 5 or {number2} > 5): {number1 > 5 or number2 > 5}")
print(f"({number1} < 10 or {number2} < 10): {number1 < 10 or number2 < 10}")
print(f"({number1} == {number2} or {number1} < 0): {number1 == number2 or number1 < 0}")

print(f"({number1} > 5 and {number2} < 10 or {number1} == {number2}): {number1 > 5 and number2 < 10 or number1 == number2}")