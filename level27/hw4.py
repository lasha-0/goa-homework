import random

numbers = list(range(1, 31))

chosen_index = random.randint(0, 29)
chosen_number = numbers[chosen_index]

while True:

    user_input = input("გთხოვთ შეიტანოთ ინდექსი (1-დან 30-მდე): ")
 
    try:
        user_index = int(user_input) - 1
    except ValueError:
        print("Incorrect, You must enter a number from 1 to 30")
        continue

    if user_index < 0 or user_index > 29:
        print("Incorrect, You must enter a number from 1 to 30")
    elif user_index == chosen_index:
        print("You guessed the number!")
        break
    else:
        print("Incorrect, Please try again")