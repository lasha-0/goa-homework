def number_check(num):
    if num > 0:
        print(f"{num} არის დადებითი რიცხვი.")
    elif num < 0:
        print(f"{num} არის უარყოფითი რიცხვი.")
    else:
        print("რიცხვი არის 0.")
        
user_input = float(input("შეიყვანეთ რიცხვი: "))
number_check(user_input)