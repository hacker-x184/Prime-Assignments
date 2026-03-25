num = int(input("Enter your number here :- "))
i =  0
while num>0:
    num=num//10
    i+=1
print("Number of digit in your number is ",i)