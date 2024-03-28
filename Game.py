import random

player_wins = 0
computer_wins = 0

def rps():
    player_choice = int(input("Choose Rock (1), Paper (2), or Scissors (3): "))
    if player_choice not in [1, 2, 3]:
        print("Invalid choice. Please enter 1, 2, or 3.")
        return rps()
    
    computer_choice = random.randint(1, 3)

    print("Computer chooses:")
    if computer_choice == 1:
        print("Rock")
    elif computer_choice == 2:
        print("Paper")
    else:
        print("Scissors")

    if player_choice == computer_choice:
        print("It's a draw!")
    elif (player_choice == 1 and computer_choice == 3) or \
         (player_choice == 2 and computer_choice == 1) or \
         (player_choice == 3 and computer_choice == 2):
        print("You win!")
        return 1
    else:
        print("Computer wins!")
        return 0

while player_wins < 2 and computer_wins < 2:
    result = rps()
    if result == 0:
        computer_wins += 1
    else:
        player_wins += 1

if player_wins == 2:
    print("Player wins 2 times!")
else:
    print("Computer wins 2 times!")
