#This is a Simple Quiz game

print(" Quiz Game ")
answer = input(" Do you want to Play the game ?? ").lower()

if answer != "yes" :
    print(" Ok Bei..")
    quit()
else :
    print(" Let's go Yeah !!!")
score = 0

quiz = input(" What country has won the most World Cups?  ").lower()
if quiz=="brazil":
    print(" Correct Answer ")
    score += 1
else :
    print(" Incorrect !!")


