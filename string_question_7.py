# in this question string ki length find kerni h ur compaire kerna h....
def any_value(string_1,string_2):
        if string_1>string_2:
            return string_1
        elif string_2>string_1:
            return string_2
        else:
            return string_1,string_2
string_1=input("please enter the any string value=")
string_2=input("please enter the any secound value=")
print(any_value(string_1,string_2))