print("Welcome to Marvel Quiz! \n")
player = input("Do you want to play this game? ").lower()
if player!= "yes":
    quit()
else:
    print("Let the games begin!!\n")

score = 0
q =0
answer = input("Which was the recent MCU movie?\n").lower()
q+=1
if answer == "quantamania":
    score +=1
    print("Correct!!")
else:
    print("Incorrect!")

answer = int(input("Whats the number of infinty stones\n"))
q+=1
if answer == 5:
    score +=1
    print("Correct!!")
else:
    print("Incorrect!")

answer = input("Which actor played Wolverine?\n").lower()
q+=1
if answer == "hugh jackman":
    score +=1
    print("Correct!!")
else:
    print("Incorrect!")

answer = input("Who killed thanos?\n").lower()
q+=1
if answer == "iron man":
    score +=1
    print("Correct!!")
else:
    print("Incorrect!")

answer = input("Which is the upcoming marvel movie?\n").lower()
q+=1
if answer == "gotg3":
    score +=1
    print("Correct!!")
else:
    print("Incorrect!")

print("Your score is "+str(score))
print("Your correct % = "+str(score/q * 100)+"%")