num = int(input("Enter your number here :- "))
sum = 0 
while num>0:
    sum = sum+(num%10)
    num = num//10
print("The sum of your number is :- ",sum)