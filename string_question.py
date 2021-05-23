def break_new_words(word):
    i=0
    a=[]
    while i<len(word):
        a.append(word[i])
        i+=1
    return a
word=input("enter the new string=")
print(break_new_words(word))
    


