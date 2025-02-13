import time

users = {}

def register():
    print("რეგისტრაციისთვის გთხოვთ შეავსოთ მონაცემები.")
    username = input("გამოიყენეთ სახელი: ")
    if username in users:
        print("ამ სახელით უკვე დარეგისტრირებულა მომხმარებელი.")
        return
    password = input("შეიყვანეთ პაროლი: ")
    users[username] = {
        "password": password,
        "balance": 0,
        "name": username,
        "email": "",
        "phone": "",
    }
    print(f"{username} წარმატებით დარეგისტრირდა.")

def reset_password():
    username = input("გთხოვთ, შეიყვანოთ თქვენი სახელი: ")
    if username not in users:
        print("მომხმარებელი არ მოიძებნა.")
        return
    new_password = input("შეიყვანეთ ახალი პაროლი: ")
    users[username]["password"] = new_password
    print(f"პაროლი წარმატებით შეიცვალა!")

def login():
    username = input("გთხოვთ, შეიყვანოთ თქვენი სახელი: ")
    if username not in users:
        print("მომხმარებელი არ მოიძებნა.")
        return None
    password = input("გთხოვთ, შეიყვანოთ პაროლი: ")
    if users[username]["password"] == password:
        print(f"{username} წარმატებით შევიდა!")
        return username
    else:
        print("პაროლი არასწორია.")
        return None

def withdraw(username):
    amount = float(input("რაოდენობა, რომელიც გსურთ გამოტანოთ: "))
    if amount <= 0:
        print("გთხოვთ, შეიყვანოთ დადებითი თანხა.")
        return
    if users[username]["balance"] >= amount:
        users[username]["balance"] -= amount
        print(f"თქვენ წარმატებით გამოიტანეთ {amount} ლარი. თქვენი ახალი ბალანსია: {users[username]['balance']} ლარი.")
    else:
        print("მიუწვდომელია საკმარისი თანხა.")

def deposit(username):
    amount = float(input("რაოდენობა, რომელიც გსურთ შეიტანოთ: "))
    if amount <= 0:
        print("გთხოვთ, შეიყვანოთ დადებითი თანხა.")
        return
    users[username]["balance"] += amount
    print(f"თქვენ წარმატებით შეიტანეთ {amount} ლარი. თქვენი ახალი ბალანსია: {users[username]['balance']} ლარი.")

def buy_item(username):
    items = {
        "1": {"name": "კომპიუტერი", "price": 1000},
        "2": {"name": "მობილური ტელეფონი", "price": 500}
    }
    
    print("გთხოვთ, აირჩიეთ ნივთი:")
    for key, item in items.items():
        print(f"{key}. {item['name']} - {item['price']} ლარი")
    
    choice = input("აირჩიეთ ნივთი (1 ან 2): ")
    if choice not in items:
        print("არასწორი არჩევანი.")
        return
    item = items[choice]
    if users[username]["balance"] >= item["price"]:
        users[username]["balance"] -= item["price"]
        print(f"{item['name']} წარმატებით იყიდეთ. თქვენი ახალი ბალანსია: {users[username]['balance']} ლარი.")
    else:
        print("მიუწვდომელია საკმარისი თანხა.")

def change_username(username):
    new_username = input("გთხოვთ, შეიყვანოთ ახალი სახელი: ")
    if new_username in users:
        print("ამ სახელით უკვე არსებობს მომხმარებელი.")
    else:
        users[new_username] = users.pop(username)
        users[new_username]["name"] = new_username
        print(f"სახელი წარმატებით შეიცვალა!")

def count_users():
    print(f"რეგისტრირებული მომხმარებლების რაოდენობა: {len(users)}")

def main_menu():
    print("ბანკის მენიუ:")
    print("1. რეგისტრაცია")
    print("2. შესვლა")
    print("3. პაროლის აღდგენა")
    print("4. მომხმარებლის სახელი შეცვალე")
    print("5. მომხმარებლების რაოდენობა")
    print("6. გამოსვლა")
    
    choice = input("აირჩიეთ ოპცია: ")
    if choice == "1":
        register()
    elif choice == "2":
        username = login()
        if username:
            user_menu(username)
    elif choice == "3":
        reset_password()
    elif choice == "4":
        username = input("გთხოვთ, შეიყვანოთ თქვენი სახელი: ")
        if username in users:
            change_username(username)
        else:
            print("მომხმარებელი არ მოიძებნა.")
    elif choice == "5":
        count_users()
    elif choice == "6":
        print("გამოსვლა...")
        time.sleep(1)
        return
    else:
        print("არასწორი არჩევანი.")
        main_menu()

def user_menu(username):
    while True:
        print(f"\n{username} - თქვენი მენიუ:")
        print("1. ფულის გამოტანა")
        print("2. ფულის შეტანა")
        print("3. ნივთის ყიდვა")
        print("4. გამოსვლა")
        
        choice = input("აირჩიეთ ოპცია: ")
        if choice == "1":
            withdraw(username)
        elif choice == "2":
            deposit(username)
        elif choice == "3":
            buy_item(username)
        elif choice == "4":
            print("გამოსვლა...")
            time.sleep(1)
            break
        else:
            print("არასწორი არჩევანი.")

if __name__ == "__main__":
    while True:
        main_menu()