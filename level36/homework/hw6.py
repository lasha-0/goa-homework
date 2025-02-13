def check_number_parity(number):
    if number % 2 == 0:
        print(f"{number} არის ლუწი")
    else:
        print(f"{number} არის კენტი")

user_input = int(input("გთხოვთ შეიყვანოთ რიცხვი: "))
check_number_parity(user_input)