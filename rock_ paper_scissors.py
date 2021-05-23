def rock_paper_scissor(user_action):
    if user_action == computer_action:
        print("Both players selected. It's a tie!")
    if user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    if user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    if user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
user_action=input("please enter user_action=")
computer_action=input("enter the computer_action=")
rock_paper_scissor(user_action)