def max_num(max_1):
    i=0
    max_2=0
    while i< len(max_1,):
        if max_1[i]>0:
            max_2=max_1[i]
        i+=1
    return (max_2)
print(max_num([1,2,3,4,5,6,7]))
