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

quiz = input(" In what country is the Chernobyl nuclear plant located?   ").lower()
if quiz=="ukraine":
    print(" Correct Answer ")
    score += 1
else :
    print(" Incorrect !!")

quiz = input(" What planet is closest to the sun?   ").lower()
if quiz=="mercury":
    print(" Correct Answer ")
    score += 1
else :
    print(" Incorrect !!")

quiz = input(" On what continent would you find the world’s largest desert?   ").lower()
if quiz=="antarctica":
    print(" Correct Answer ")
    score += 1
else :
    print(" Incorrect !!")

print(" Quiz completed !! ")
print(" Congratulations !! You've got " + str(score) + " Points" )