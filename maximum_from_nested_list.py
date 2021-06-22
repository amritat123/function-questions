
def max_num(num_1):
    i=0
    while i<len(num_1):
        j=0
        max=0
        a=num_1[i]
        while j<len(a):
            if a[j]>max:
                max=a[j]
            j+=1 
        print(max)
        i+=1      
max_num([[2,4,6,81,0],[1,3,5,17,9]])