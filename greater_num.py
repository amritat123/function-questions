def greater_number(num,num1,num2):
    if num>num1 and num>num2:
        print("num bada hai")
    elif num1>num and num1>num2:
        print("num1 sbhse bada h ")
    elif num2>num and num2>num1:
        print("num2 is greater")
    else:
        print("all are equal")
num=int(input("enter the any num="))
num1=int(input("enter the secund num1="))
num2=int(input("please enter the third num2="))
greater_number(num,num1,num2)