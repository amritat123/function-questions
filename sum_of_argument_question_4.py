# Question 4
# Yeh question 2 parts mein hai. Dono parts ka code same file mein likh ke submit karein.
#Question (Part 1)
#add_numbers naam ka function likhiye jo do numbers ko arguments ke tarah le aur fir unka sum print karta hai. Arguments ka naam number1 aur number2 hona chaiye. Input

def add_number(num1,num2):
    print(num1+num2)
add_number(60,70)

#Question (Part 2)
#add_numbers_list naam ka function likhiye jo do integers ki 2 lists leta ho aur fir same position wale integers ka sum print karta ho. Same position waale 2 integers ka sum karne ke liye Part 1 mein di gayi add_numbers waale function ka use karo. Jaise agar hum iss function ko [50, 60, 10] aur [10, 20, 13] denge ko woh yeh print kareg

def add_number(list1,list2):
    sum=0
    i=0
    while i<len(list1):
        sum=list1[i]+list2[i]
        print(sum)
        i+=1 
list1=[2,4]
list2=[5,6]
add_number(list1,list2)













    





