def merge(list1,list2):
    for i in list1:
        for j in list2:
            if(i!=j):
                list1.append(list2)
                print(list1.append(list2))
            else:
                print(list1)
                continue
    return list1
lis1=[12,334,54,56,32,45,54]
lis2=[34,54,56,32,98,67,64,34]
merge(lis1,lis2)
         