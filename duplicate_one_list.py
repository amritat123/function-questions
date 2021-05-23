def two_list(number,number1):
    list1=[]
    i=0
    while i<len(number):
        if number[i]  in number1:
            list1.append(number[i])
            list1.sort()
        i+=1
    print(list1)
two_list([1, 342, 75, 23, 98],[75, 23, 98, 12, 78, 10, 1])
