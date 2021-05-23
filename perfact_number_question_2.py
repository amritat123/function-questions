# def perfect_number(perfact):
#     i=1
#     sum=0
#     while i<numbers:
#         if (numbers%i==0):
#             sum=sum+i
#         i+=1
#     if sum==numbers:
#         print("this is perfact number")
#     else:
#         print("not perfact number")
# numbers=int(input(" please enter the number"))
# perfect_number(numbers)   

#perfact_number in between (1 to1000)
def perfact_number(number):
    i=1
    while i<1000:
        sum=0
        j=1
        while j<i:
            if i%j==0:
                sum=sum+j
            j+=1
        if sum==i:
            print(i,"perfact number")
        i+=1
perfact_number(1000)

#agar user input mai koi bhi number dale to vaha tak (perfact number) bataye...
# def perfect(user):
#     i=1
#     while i<user:
#         sum=0
#         j=1
#         while j<i:
#             if j%i==0:
#                 sum=sum+j
#             j=j+1
#         if sum==i:
#             print(i,"perfct no")
#         i+=1
# user=int(input("enter the number"))   
# perfect(user)


