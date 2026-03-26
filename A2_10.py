import random
com  =  random.randint(0,100)
while True:
    num = int(input("Gussa a Number here:-"))
    if (com>num):
        print("the guess is above the number")
    elif(com==num):
        print("The Guess is correct :-)!")
        break
    elif(com<num):
        print("the guess is below the number")