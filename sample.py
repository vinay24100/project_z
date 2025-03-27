import random

# Function to print a welcome message
def welcome_message():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess it?")

# Function to play the game
def play_game():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    
    # Set the number of attempts
    attempts = 0
    
    # Start the game loop
    while True:
        try:
            # Ask the user to guess the number
            user_guess = int(input("Enter your guess: "))
            attempts += 1
            
            # Check if the guess is correct, too high, or too low
            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid integer.")

# Main function to start the game
def main():
    welcome_message()
    play_game()

# Run the main function
if __name__ == "__main__":
    main()

