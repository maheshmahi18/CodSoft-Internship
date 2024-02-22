import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

# Main program loop
while True:
    user_score = 0
    computer_score = 0
    rounds = 0

    print("Welcome to Rock-Paper-Scissors Game!")

    while True:
        print("\nRound:", rounds + 1)
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        computer_choice = random.choice(['rock', 'paper', 'scissors'])

        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please enter rock, paper, or scissors.")
            continue

        print("Your choice:", user_choice)
        print("Computer's choice:", computer_choice)

        result = determine_winner(user_choice, computer_choice)
        print("Result:", result)

        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1

        rounds += 1

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Final Scores:")
            print("Your score:", user_score)
            print("Computer's score:", computer_score)
            break

    play_again = input("Do you want to start a new game? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thank you for playing Rock-Paper-Scissors. Goodbye!")
        break
