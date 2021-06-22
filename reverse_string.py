def my_string(value):
    str1=""
    i=0
    i=len(value)
    while i>0:
        str1+=value[i-1]
        i-=1
    return str1
print(my_string("1234abcd"))
