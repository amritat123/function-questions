def remove_dublicate():
    d=list1+list2
    i=0
    b=[]
    while i<len(d):
        if d[i] not in b :
            b.append(d[i])
        i=i+1
    print(b)
list1 = [1, 5, 10, 12, 16, 20]
list2 = [1, 2, 10, 13, 16] 
remove_dublicate()