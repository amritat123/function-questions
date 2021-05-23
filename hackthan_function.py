# def driver(speed):
#     if speed<70:
#         print("ok")
#     else:
#         speed1=(speed-70)//5
#         if speed1>12:
#             print("license suspended")
#         else:
#             print("point=",speed1)
# speed=int(input("enter the speed"))
# driver(speed)

# def sum_list(num):
#     sum=0
#     i=0
#     while i<len(num):
#         sum+=num[i]
#         i+=1
#         return sum
# print(sum_list([1,2,3,4,5,6]))


#sum qustion in function..
# def total_sum(num):
#     i=1
#     count=0
#     while i<=num:
#         user=int(input('enter the number'))
#         count+=user
#         i+=1
#     return count
# print(total_sum(5))


# divisible hai ya nhi qustion in function..
# def count(num):
#     i=1
#     while i<num:
#         if num%2==0:
#             return num,"divisible hai"
#         if num%2!=0:
#             return num,"divisible nahi hai"
#         i+=1
# print(count(num=int(input("enter num")))


# #function even number with return..
# def even_number(num):
#     i=1
#     sum=0
#     while i<=num:
#         if i%2==0:
#             sum+=1
#         i+=1
#     return sum
# print(even_number(10))


#function odd number with return..
# def odd_number(num):
#     i=1
#     sum=0
#     while i<=num:
#         if i%2!=0:
#             sum+=1
#         i+=1
#     return sum
# print(odd_number(25))


#in function factorial number..
# def factorial(num):
#     i=1
#     while num>0:
#         i=i*num
#         num=num-1
#     return i
# num=int(input("enter the number"))
# print(factorial(num))


#maximum number in loop function...
# def total_number(num):
#     max=0
#     i=0
#     while i<len(num):
#         if num[i]>max:
#             max=num[i]
#         i+=1
#     return max
# print(total_number([50,70,90,8,6,45,23]))


# #minimum number in function..
# def total_number(num):
#     min=num[0]
#     i=0
#     while i<len(num):
#         if num[i]<min:
#             min=num[i]
#         i+=1
#     return min
# print(total_number([70,80,45,67,8,67,55]))
# table in function..
# def number(table):
#     i=1
#     a=0
#     while i<=10:
#         a=table*i
#         i+=1
#     return a

# sum os 3 and 5 numbers in functions..
# def num(limit):
#     i=0
#     sum=0
#     while i<limit:
#         if i%3==0:
#             sum+=1
#         if i%5==0:
#             sum+=1
#         i+=1
#     return sum
# limit=int(input("enter the number "))
# print(num(limit))

# #reverse number in function..
# def number(reverse):
#     i=1
#     z=[]
#     while i<=len(reverse):
#         z.append(reverse[-i])
#         i=i+1
#     return z
# print(number([5,8,9,10,4,3]))


# 20 se 40 ke beetch number nikalne thy in fuction..
# def num(n):
#     count=0
#     i=0
#     while i< len(n):
#         if n[i]>20 and n[i]<40:
#             count+=1
#         i+=1
#     return count
# print(num([50,40,23,70,56,35,25,12,5,10,7]))


# #square of element(list) in function..
# def my_list(element):
#     i=0
#     a=[]
#     while i<len(element):
#         b=element[i]*element[i]
#         a.append(b)
#         i+=1
#     return a
# print(my_list([4,5,6,7,8,9,12]))


# square of elements in secund way in function..
# def my_list(element):
#     i=0
#     a=[]
#     while i<len(element):
#         b=element[i]*element[i]
#         a.append(b)
#         i=i+1
#     return a
# element=[4,5,6,7,8,9,12]
# print(my_list(element))



