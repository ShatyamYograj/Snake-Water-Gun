import random

# 1 for snake
# -1 for water
# 0 for gun

computer= random.choice([-1, 0, 1])
youstr= input("Enter Your Choice: ")
youDict= {"s":1, "w": -1, "g": 0}
reverseDict= {1: "Snake", -1: "Water", 0: "Gun"}


you= youDict[youstr]

# By now we have two numbers (variables), you and computer

print(f"You choose { reverseDict[you]}\nComputer choose {reverseDict[computer]}")
if(computer == you):
    print("Its a draw")

else:
    if(computer == -1 and you== 1):
        print("You Win!")
    elif(computer == -1 and you== 0):
        print("You Lose!")
    elif(computer == 1 and you== -1):
        print("You lose!")
    elif(computer == -1 and you== 0):
        print("You Win!")
    elif(computer == 0 and you== 1):
        print("You lose!")
    elif(computer == 0 and you== -1):
        print("You Win!")
    else:
        print("Something went wrong!")
    