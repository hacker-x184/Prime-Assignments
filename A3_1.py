p = input("Enter Your Word here:- ")
for i in range(0,len(p)):
    if (p[i]==p[-(i+1)]):
        is_palindrome = True
    else:
        is_palindrome = False
if is_palindrome:
    print("Your Given Word is palindrome")
else:
    print("Your Given Word is not palindrome")



