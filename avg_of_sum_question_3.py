# in this user mai koi bhi number dale vo vha tak chale ur unn sabka sum sum or averge print kere..

def sum_number(number):
    i=0
    sum=0
    while i<number:
        num=int(input('enter the any number'))
        sum=sum+num
        avg=sum/num
        i+=1
    print(sum)
    print(avg)
num_1=int(input("please enter the number"))
sum_number(num_1)

