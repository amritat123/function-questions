def sum_value(number):
    sum=0
    i=0
    while i<len(number):
        sum=sum+number[i]
        i+=1
    return sum
print(sum_value((2,3,4,5,5)))


