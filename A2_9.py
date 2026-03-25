def isprime(num):
    temp=num-1
    result =""
    while temp>=2:
        if (num%temp==0):
            result ="not prime"
            return result
        temp-=1
    if result != "not prime":
        result = "prime"
        return result
num = int(input("Enter your number here:--"))
print("Your given number is a ",isprime(num))
