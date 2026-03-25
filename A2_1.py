salary = float(input("Enter your salary here :- "))
if (salary<30000):
    print("Your final tax you need to pay is ", (salary*0.05))
elif(salary>30000 or salary<70000):
    print("Your final tax you need to pay is ", (salary*0.15))
else:
    print("Your final tax you need to pay is ", (salary*0.25))

