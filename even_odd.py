#check_numbers naam ka ek function likhiye jo do numbers le aur fir print kare "Dono even hain" agar dono numbers even (2 se divide hote ha
def check_number(even,even1):
        if even%2==0 and even1%2==0:
            print("even number")
        else:
            print("even number nhi h")
even=int(input (" any number"))
even1 =int(input("enter number"))
check_number(even,even1)

#  Question (Part 2)
#Ab ek check_numbers_list naam ka ek function likho jo inetgers ki list ko arguments ki tarah le aur fir check kare ki same index waale dono integers even hain ya nahi. Yeh check karne ke liye pichle Part 1 mein likhe check_numbers function ka use karo. Agar aapne apne function ko [2, 6, 18, 10, 3, 75] aur [6, 19, 24, 12, 3, 87] Toh usko yeh output deni chaiye:  
def check_number(a,b):
    i=0
    while i<len(a):
        if a[i]%2==0 and b[i]%2==0:
            print("even number hai")
        else:
            print("even nhi hai")
        i+=1
a= [1,4,6,8,9]  
b= [1,4,8,8,10]   
print(check_number(a,b)) 
