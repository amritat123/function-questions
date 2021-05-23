def add(a,b):
    return (a+b)
def sub(a,b):
    return (a-b)
def multiply(a,b):
    return (a*b)
def div(a,b):
    return (a/b)
def f_div(a,b):
    return (a//b)
def main():
    if symbol=="+":
        print(add(4,5))
    elif symbol=="-":
        print(sub(7,4))
    elif symbol=="*":
        print(multiply(6,4))
    elif symbol=="/":
        print(div(4,2))
    elif symbol=="//":
        print(f_div(4,2))
    else:
        pass
symbol=input("enter symbol ")
main()