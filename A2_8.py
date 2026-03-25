result = 0 
while True:    
    num1 = int(input("Enter your number here :- "))
    num2 = int(input("Enter your number here :- "))
    opp = input("Chocie Your Opereation from below:-\n'+'-Addditin\n'-'-Subtraction\n'*'-Multiplication\n'/'-Division\nEnter the Operater accoring to your operation:-- ")
    if (opp=="+"):
        result = num1+num2
        print(result)
    elif(opp=="*"):
        
        result=num1*num2
        print(result)
    elif(opp=="-"):
        
        result = num1-num2
        print(result)
    elif(opp=="/"):
        
        result=num1/num2
        print(result)
    elif(opp.lower()=="y"):
        continue
    else:
        break
