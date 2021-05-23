#question number_1:-

def eligible_for_vote(voter):
    if voter_age>=18:
         print("he can eligible vote")
    else:
        print("he  is not deligible vote")
voter_age=int(input("enter the he or she age"))
eligible_for_vote(voter_age)