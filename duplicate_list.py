# string_list = ["Rishabh", "Rishabh", "Abhishek", "Rishabh", "Divyashish", "Divyashish"]
def string_list(name):
    list_1=[]
    i=0
    while i<len(name):
        if name[i] not in list_1:
            list_1.append(name[i])
        i+=1
    return list_1
print(string_list(["Rishabh", "Rishabh", "Abhishek", "Rishabh", "Divyashish", "Divyashish"]))