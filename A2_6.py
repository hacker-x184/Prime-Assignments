list=[]
for i in range (0,101):
    if (i%3==0 and i%5==0):
        list.append(i)
        print("This nuber is divisible by 3 and 5 both",i)
print("Here are the list of all the number between 1 to 100 that was divisible by both 3 ann 5\n",list)