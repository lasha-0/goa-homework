my_list =  [2, 4, 5, 6, 9, 10, 13, 17, 18, 19]
for number in my_list:
    if number % 5 == 0:
        print(f"{number} - ხუთის ჯერადია")
    elif number % 3 == 0:
        print(f"{number} - სამის ჯერადია")
    else:
        print(f"{number}")