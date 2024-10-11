import random

# Initialize win counters for player and computer
player_wins = 0
computer_wins = 0

# Main game loop that runs until one wins two rounds
while player_wins < 2 and computer_wins < 2:
    choices = ["rock", "paper", "scissors"]
    winners = ["Player", "Tie", "Computer"]

    print("Let's play rock, paper, or scissors")
    
    # Get player choice and randomly generate computer choice
    player_choice = input("Choose rock, paper or scissors: ").lower()
    computer_choice = random.choice(choices)
    
    print(f'Computer chose: {computer_choice}')
    
    # Determine the winner based on the choices
    if (player_choice == "rock" and computer_choice == "scissors") or (player_choice == "scissors" and computer_choice == "paper") or (player_choice == "paper" and computer_choice == "rock"):
        winner = winners[0]
    elif (player_choice == "scissors" and computer_choice == "rock") or (player_choice == "paper" and computer_choice == "scissors") or (player_choice == "rock" and computer_choice == "paper"):
        winner = winners[2]
    else:
        winner = winners[1]
    
    # Print the result and update the win counters
    if winner == "Player":
        print("Player wins this round")
        player_wins += 1
    elif winner == "Computer":
        print("Computer wins this round")
        computer_wins += 1
    else:
        print("It's a tie")

# Final game result
if player_wins == 2:
    print("Player wins the game!")
else:
    print("Computer wins the game!")
