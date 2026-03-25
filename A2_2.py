num1 = int(input("Enter your number 1 value here :- "))
num2 = int(input("Enter your number 2 value here :- "))
i = num1
even=[]
for i in range(num1,num2):
    if (i%2!=0):
        print("Even number",i)
        even.append(i)
    else:
        continue
    i+=i
print(even)