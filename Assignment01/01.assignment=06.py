import random

print("Let's Play Rock, Paper, Scissor game!")

choices = ["rock", "paper", "scissor"]
draw_count = comp_count = user_count = 0

while True:
    user = input("Enter rock, paper, or scissor: ").lower()
    if user not in choices:
        print("Invalid choice, try again.")
        continue

    comp = random.choice(choices)
    print("Computer choose:", comp)

    if user == comp:
        print("It's a draw!")
        draw_count += 1
    elif (user == "rock" and comp == "scissor") or \
         (user == "paper" and comp == "rock") or \
         (user == "scissor" and comp == "paper"):
        print("You win!")
        user_count += 1
    else:
        print("You lose!")
        comp_count += 1

    if input("Play again? (Y/N): ").upper() != 'Y':
        break

print()
print('Results: ')
print('You won:', user_count, 'times')
print('Computer won:', comp_count, 'times')
print('Draw:', draw_count, 'times')

