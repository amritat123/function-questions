def outer_fun():
    def inner_fun(a,b):
        print(a+b+5)
    inner_fun(4,6)
outer_fun()
