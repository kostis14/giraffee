import random
Number = random.randint(1,9)
answer = ""
num = 0
print(Number)
yer = ""
while answer != "exit" and Number != yer:
    yer = int(input("Try and guess!"))
    num = num + 1
    if yer > Number:
        print("You guessed too high..")
    elif yer < Number:
        print("You guessed too low..")
    else:
        print("Correct!")
    answer = input("Try again?\n (or exit)")
print("You got the number in ", num , " Guesses!")