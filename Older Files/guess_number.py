import random as r
def user_guess():
    print("Lets see your guessing powers!\n")
    topmost = int(input("Enter the max in range\n"))
    count =0
    if topmost<=0:
        print("topmost should be greater than 0")
        quit()
    num = r.randint(1,topmost)
    while True:
        count +=1
        guess = int(input("Whats your guess!\n"))
        if guess<=0:
            print("Your guess should be greater than 0")
            continue
        if guess==num:
            print("Congratulations your guess is correct")
            break
        elif guess<num:
            print("Your guess is lesser than the number")
        else:
            print("Your guess is greater than the number")

    print("You got the answer in",count,"attempts")

def comp_guess(x):
    low =1
    high=x # here x is the topmost number in the range
    guesses =0
    while True:
        if low==high:
            print("Your number is ",high)
            break
        guess = r.randint(low,high)
        direction = input(f"Enter l if the guessed number {guess} is lower than the actual guess, h for higher and c for correct:\n").lower()
        if direction=='l':
            low=guess+1
            guesses+=1
        elif direction=='h':
            high=guess-1
            guesses+=1
        elif direction =='c':
            guesses+=1
            print("Your number is "+str(guess)+" I got it in "+str(guesses)+" guesses")
            break

comp_guess(100)

