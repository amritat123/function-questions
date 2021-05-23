 #in this question user mai koi bhi number dale to vahi tak even or odd bataye
 def show_number(limit):
    i=0
    sum=0
    while i<limit:
        if i%2==0:
            print(i,"even number hai")
        else:
            print(i,"odd nmuber hai")
        i+=1
num=int(input("any starting value"))
show_number(num)