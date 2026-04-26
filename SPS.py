import random
print("STONE PAPER SCISSOR GAME")
choices = ["stone", "paper", "scissor"]
while True:
    user = input("\nEnter your choice (stone/paper/scissor): ").lower()
    if user not in choices:
        print("Invalid choice! Try again.")
        continue
    computer = random.choice(choices)
    print("Computer chose:", computer)
    if user == computer:
        print("It's a DRAW!")
    elif (user == "stone" and computer == "scissor") or \
         (user == "paper" and computer == "stone") or \
         (user == "scissor" and computer == "paper"):
        print("You WIN!")
    else:
        print("You LOSE!")
    again = input("Play again? (yes/no): ").lower()
    if again != "yes":
        print("Game Over!")
        break
