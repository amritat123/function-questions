def all_number(number):
    i=0
    a=[]
    b=[]
    while i<len(number):
        if number[i]%2==0:
            a.append(number[i])
        else:
            b.append (number[i])
        i+=1
    print(a)
    print(b)
all_number([1,2,3,4,5,6,7,8,9,10])