import random as r
options = ["r", "p", "s"]
uw=0
cw=0
chances=5
for i in range(5):
    
    userChoice = input("r,p,s")
    compChoice = r.choice(options)
    print("You chose: ", userChoice)   
    print("Computer chose: ", compChoice)
    print("Chances:",chances)
    print("Your wins:",uw)
    if userChoice == compChoice: 
            print("It's a tie!") 
    elif userChoice == "r" and compChoice == "sc":             
            print("You win!")
            uw+=1
    elif userChoice == "p" and compChoice == "r": 
            print("You win!")
            uw+=1
    elif userChoice == "sc" and compChoice == "p": 
            print("You win!")
            uw+=1
    else: 
        print("Computer wins!")
        cw+=1
    chances-=1
if uw>cw:
    print("😎")
elif uw==cw:
    print("It's a tie")
else:
    print("Get ready for war aginest AI 🫡")