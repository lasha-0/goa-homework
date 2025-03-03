def dots_calculator(equation):
    dots1, operator, dots2 = equation.split()
    
    num1, num2 = len(dots1), len(dots2)

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "//":
        result = num1 // num2 if num2 != 0 else 0
    
    return "." * result if result != 0 else ""