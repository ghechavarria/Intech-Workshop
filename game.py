import random

def get_computer_move():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(player, computer):
    if player == computer:
        return "tie"
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'paper' and computer == 'rock') or \
         (player == 'scissors' and computer == 'paper'):
        return "player"
    else:
        return "computer"

def main():
    player_score = 0
    computer_score = 0

    print("Welcome to Rock, Paper, Scissors! Type 'quit' to exit.")

    while True:
        player_move = input("Choose rock, paper, or scissors: ").lower()
        if player_move == 'quit':
            break
        if player_move not in ['rock', 'paper', 'scissors']:
            print("Invalid move. Try again.")
            continue

        computer_move = get_computer_move()
        print(f"Computer chose: {computer_move}")

        winner = determine_winner(player_move, computer_move)
        if winner == "tie":
            print("It's a tie!")
        elif winner == "player":
            print("You win this round!")
            player_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print(f"Score - You: {player_score} | Computer: {computer_score}\n")

    print("Game over!")
    print(f"Final Score - You: {player_score} | Computer: {computer_score}")

if __name__ == "__main__":
    main()