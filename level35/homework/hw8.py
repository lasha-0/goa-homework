def greet_user():
    რიღხვი = int(input("შეიყვანეთ რიღხვი: "))
    if რიღხვი > 0:
        print("დადებითია")
    elif რიღხვი < 0:
        print("უარყოფითი")
    else:
        print("ნულოვანი") 

greet_user()