import random
num=1
print("Welcome to the Number Guessing Game!, we here have 10 attempts!!")
print("The secret no is between 1 to 50:")
attempts=10
secretno=random.randint(1,50)
guesscorrect=False

while num<=10:
    print(f"You have {attempts} attempts left")
    userno=int(input("Enter your guess: "))
    if userno==secretno:
        print("You guessed correctly!")
        guesscorrect=True
        break
    else:
        if userno<secretno:
            higher_or_lower="higher"
        else :
            higher_or_lower="lower"
    print(f"You guessed incorrectly! Try {higher_or_lower} number.")

    num+=1
    attempts=attempts-1
if guesscorrect==False:
    print("Better luck next time!!.")
print(f"The secret no was {secretno}.GAME OVER!!!")

