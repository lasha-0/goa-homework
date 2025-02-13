def calculate_quotient(num1, num2):
    if num2 != 0:
        print(f"განაყოფი: {num1 / num2}")
    else:
        print("გთხოვთ, მეორე რიცხვი არ იყოს ნული!")

num1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
num2 = float(input("შეიყვანეთ მეორე რიცხვი: "))

calculate_quotient(num1, num2)