#kBC game in function.....
que_list = ["How many continents are there?","What is the capital of India?","NG mei kaun se course padhaya jaata hai"]
opt_list = [["Four", "Nine", "Seven", "Eight"],["Chandigarh", "Bhopal", "Chennai", "Delhi"],["Software Engineering", "Counseling", "Tourism", "Agriculture"]]
ans_list = [3, 4, 1] 
fifty_list = [['Four','seven'],['Bhopal','Delhi'],['Software Engineering','Counseling']]
sol_list=[2,2,1]
lifeline_c=0
def lifeline(index):
    global lifeline_c
    j=0
    if lifeline_c==0:
        while j<len(fifty_list[index]): 
            print(j+1,fifty_list[index][j])
            j+=1
        user_ans=int(input("enter the answer"))
        lifeline_c+=1
        if user_ans==sol_list[index]:
            return True
        else:
            return False
    else:
        print("you already used 5050")
        print("you have only one chance")
        # return "no"
def option(index):
    j=0
    while j<len(opt_list[index]):
        print(j+1,opt_list[index][j])
        j+=1
    user_ans=int(input("enter the option"))
    if user_ans==ans_list[index]:
        return True
    if user_ans==5050:
        return (lifeline(index))
    else:
        return False
def que():
    i=0
    while i<len(que_list):
        print("Q",i+1,que_list[i],"?")
        result=option(i)
        if result==True:
             print("congratulation")
        else:
            print("you are loser")
            break
        i+=1
def main():
    que()
main()


