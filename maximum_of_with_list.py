
def max_num(num_1,num_2):
    i=0
    max=0
    while i<len(num_1):
        a=num_1+num_2
        if a[i]>0:
            max=a[i]
        i+=1
    return max        
print(max_num([2,4,6,8,10],[1,3,5,7,9]))