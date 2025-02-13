number = int(input("შეიყვანეთ რიცხვი: "))
even_sum = 0
for i in range(2, number + 1, 2):
    even_sum += i
print(f"ლუწი რიცხვების ჯამი არის: {even_sum}")