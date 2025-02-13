def divide_numbers():
    number1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
    number2 = float(input("შეიყვანეთ მეორე რიცხვი: "))
 
    if number2 != 0:
        result = number1 / number2
        print(f"გაყოფის შედეგი: {result}")
    else:
        print("ვერ შეიძლება გაყოფა ნულით!")

divide_numbers()