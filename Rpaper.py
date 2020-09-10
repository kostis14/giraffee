import tkinter


def result(answer1, answer2):
    if answer1 == "paper" and answer2 == "rock" or answer1 == "rock" and answer2 == "scissors" or answer1 == "scissors" and answer2 == "paper":
        print("Player 1 Wins!")
    elif answer2 == "paper" and answer1 == "rock" or answer2 == "rock" and answer1 == "scissors" or answer2 == "scissors" and answer1 == "paper":
        print("Player 2 Wins!")
    else:
        "Tie."




play = input("Would you like to play").lower()

while play != "no" and play == "yes":

    while True:
        answer1 = input("Provide me with a choice\n")
        if answer1 == "rock" or answer1 == "paper" or answer1 == "scissors":
            break
        else:
            print("Please provide a correct input")

    while True:
        answer2 = input("And you.\n").lower()
        if answer2 == "rock" or "paper" or "scissors":
            break
        else:
            print("Please provide a correct input")
    result(answer1, answer2)
    print("Would you like to play again? (YES/NO)")
    play = input().lower
