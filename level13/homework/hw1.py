number1 = float(input("გთხოვთ, შეიყვანოთ პირველი რიცხვი: "))
number2 = float(input("გთხოვთ, შეიყვანოთ მეორე რიცხვი: "))

sum_result = number1 + number2
difference_result = number1 - number2
product_result = number1 * number2
quotient_result = number1 / number2 if number2 != 0 else "გაუძლო არ შეიძლება ზეროიანი რიცხვი"

print(f"ჯამი: {sum_result}")
print(f"განსხვავება: {difference_result}")
print(f"პროდუქტი: {product_result}")