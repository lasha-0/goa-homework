def coffee_script(num):
    if num % 3 == 0 and num % 4 == 0:
        return "CoffeeScript" if num % 2 == 0 else "Coffee"
    elif num % 3 == 0:
        return "JavaScript" if num % 2 == 0 else "Java"
    return "mocha_missing!"