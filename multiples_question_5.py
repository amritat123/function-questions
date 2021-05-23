def new_number(limit):
    i=1
    sum=0
    while i<=limit:
        if i%3==0 or i%5==0:
            sum=sum+i
        i+=1
    print(sum)          
limit=int(input("please enter the number"))
new_number(limit)