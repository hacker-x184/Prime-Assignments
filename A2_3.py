num = int(input("Enter your number here :- "))
digits = []
while num > 0:
    digits.append(num % 10) 
    num //= 10    

for digit in reversed(digits):
    print(digit)