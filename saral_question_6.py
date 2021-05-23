#question number_6
# question number_6(part_1)
def calculater(number_x,number_y):
    if symbol== "+":
        print("addition",number_x+number_y)
    elif symbol=="-":
        print("substractin",number_x-number_y)
    elif symbol=="%":
        print(number_x% number_y)
    elif symbol=="//":
        print(number_x //number_y)
    elif symbol=="/":
        print(number_x / number_y)
    elif symbol=="*":
        print(number_x *number_y)
    else:
        print(number_x**number_y)
symbol=input("enter the any symbol")
number_x=int(input("enter the any value"))
number_y=int(input("any secound value"))
calculater(number_x,number_y)  

