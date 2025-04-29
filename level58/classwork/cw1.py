def modify_and_subtract(a, b):
    if a % 2 == 0:
        a = a // 2
    else:
        a = a + 1
    return a - b
