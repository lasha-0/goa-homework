def check_age(birth_year):
    current_year = 2025
    age = current_year - birth_year
    
    if age >= 18:
        return "თქვენ სრულწლოვანი ხართ."
    else:
        return "თქვენ არ ხართ სრულწლოვანი."
birth_year = int(input("შეიყვანეთ თქვენი დაბადების წელი: "))
print(check_age(birth_year))