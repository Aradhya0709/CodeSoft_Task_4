import random

# Function to get computer's choice
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

# Function to display the results
def display_result(user_choice, computer_choice, winner):
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win!")
    else:
        print("Computer wins!")

# Main game function
def play_game():
    user_score = 0
    computer_score = 0
    
    while True:
        print("\nRock-Paper-Scissors Game")
        print("Type 'rock', 'paper', or 'scissors' to play.")
        print("Type 'exit' to quit the game.")

        user_choice = input("Your choice: ").lower()
        
        if user_choice == 'exit':
            print("Exiting the game. Final score:")
            print(f"Your score: {user_score}")
            print(f"Computer's score: {computer_score}")
            break

        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice! Please choose 'rock', 'paper', or 'scissors'.")
            continue

        # Get computer's choice
        computer_choice = get_computer_choice()

        # Determine the winner
        winner = determine_winner(user_choice, computer_choice)

        # Display the result
        display_result(user_choice, computer_choice, winner)

        # Update scores
        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1

        # Show current scores
        print(f"\nCurrent Score - You: {user_score} | Computer: {computer_score}")
        
        # Ask to play again
        play_again = input("\nDo you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thank you for playing! Final score:")
            print(f"Your score: {user_score}")
            print(f"Computer's score: {computer_score}")
            break

# Run the game
if __name__ == "__main__":
    play_game()
