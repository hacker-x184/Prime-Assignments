def checklist(l1,l2):
    found = False
    for i in range (len(l1)):
        for j in range (len(l2)):
            if l1[i]==l2[j]:
                found = True
                break
    if found:
        print(f"Common element exits {l1},{l2}")
    else:
        print(f"No Common element exits {l1},{l2}")
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
list3 = [1, 2, 3] 
list4 = [3, 4]
checklist(list1,list2)
checklist(list3,list4)