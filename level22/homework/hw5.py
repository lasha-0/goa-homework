n = int(input("გთხოვთ, შეიყვანოთ რიცხვი: "))

product = 1
for i in range(1, n+1):
    product *= i
    print(f"{i} - ნამრავლი: {product}")