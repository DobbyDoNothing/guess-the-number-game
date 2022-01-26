import random

number = random.randint(1,10)

chance = 5

while chance > 0:
    guess = int(input("Enter a number in between 1 & 10 : ") )

    if guess==number:
        print("Well done! You guessed correct! You used " , 5-chance , " chances!")
        break

    elif guess < number:
        print("Your guess was too low. Try a higher number than --> " , guess)
    
    else:
        print("Your guess was too high. Try a lower number than --> ", guess)


    chance -= 1

if chance == 0:
    print("Sorry, you lost. Better luck next time! You used 5 chances!")


