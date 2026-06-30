def NumSameEle(list):
    seen = set()
    duplicate = set()
    for i in list:
        if i in seen:
            duplicate.add(i)
        else:
            seen.add(i)
    print(f"Here are the list of the elemt that appere more than ones {duplicate}")



list = [12, 7, 3, 15, 7, 9, 21, 3, 18, 12, 25, 9, 30, 14, 21, 5, 18, 11, 25, 7]
NumSameEle(list)