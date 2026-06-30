def FindUnique(str):
    dublicate = set()
    unique = set()
    for i in str:
        if i in unique:
            dublicate.add(i)
        else:
            unique.add(i)
    print(f"here are all unique {unique},They are the total no of unique characteres :{len(unique)}")
    print(f"here are all dublicate {dublicate},They are the total no of dublicate characteres :{len(dublicate)}")
str = input("Enter your sring here:-")
FindUnique(str)