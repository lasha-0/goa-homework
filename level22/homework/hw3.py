n = int(input("შეიყვანეთ რიცხვი: "))

sum_of_squares = sum(i**2 for i in range(1, n+1))

print(f"1-დან {n}-მდე რიცხვების კვადრატების ჯამი: {sum_of_squares}")