num = int(input("შეიტანეთ რიცხვი: "))

sum_of_multiples = 0

for i in range(1, num+1):
    if i % 2 == 0:
        sum_of_multiples += i

print("ორზე ნამრავლების ჯამი არის:", sum_of_multiples)