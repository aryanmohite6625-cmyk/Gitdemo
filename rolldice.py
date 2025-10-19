import random
print("WELCOME TO A GAME OF ROLLING A DICE")
while True:
    choice = input("press 'Enter' to roll the dice or press 'q' to quit: ")
    choice = choice.strip()
    if choice == "q":
        print("Thank you for playing")
        break
    elif choice == "":
        roll = random.randint(1,6)
        print(f"Your no is {roll}")
    else :
        print("invalid choice")
print("GAME OVER!!!")