def max_num(max_1):
    i=0
    max=0
    while i< len(max_1,):
        if max_1[i]>max:
            max=max_1[i]
        i+=1
    return (max)
print(max_num([1,2,3,4,5,6,7]))
