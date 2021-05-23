 factorial(num):
    fact=1
    while num>0:
        fact=fact*num
        num=num-1
    print(fact)
num=int(input("enter the number="))
factorial(num)