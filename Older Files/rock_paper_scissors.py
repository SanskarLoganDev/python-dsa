import random as r
print("Welcome to the rock paper scissors game!!\n")
comp_wins=0
user_wins=0
l=["rock","paper","scissors"]

while True:
    comp_input = r.choice(l)
    user_input = input("What're you gonna play\n(press q to quit)\n").lower()
    if user_input=="q":
        break
    if user_input not in l:
        print("Only rock paper scissors mate!")
        continue
    if user_input==comp_input:
        print("SAME!!!!")
        continue
    elif user_input=="rock" and comp_input=="scissors":
        print("You've won!!")
        user_wins+=1
        continue
    elif user_input=="scissors" and comp_input=="paper":
        print("You've won!!")
        user_wins+=1
        continue
    elif user_input=="paper" and comp_input=="rock":
        print("You've won!!")
        user_wins+=1
        continue
    else:
        print("You've lost!!")
        comp_wins+=1
        continue
print("Reults: Comp",comp_wins,"& User",user_wins)
if comp_wins>user_wins:
    print("Computer has won!")
elif comp_wins<user_wins:
    print("You've won")
else:
    print("Its a tie")    