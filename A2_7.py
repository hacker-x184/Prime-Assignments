while True:
    num = input("If you want to close the programe type 'quit':)\nEnter your number here:-")
    if num.lower() =="quit":
        break
    else:
        num = float(num)
        if (num>0):
            print("Your Number is Postive\nHere is your number",num)
        elif(num<0):
            continue
        elif(num==0):
            print("Your given number is zero")
        

