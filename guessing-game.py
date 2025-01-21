import random

def guessing_game():
    number = random.randint(1, 100)
    attempts = 0

    print("🎯 Welcome to the Guessing Game!")
    print("I've chosen a number between 1 and 100. Can you guess it?")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number:
                print("📉 Too low! Try again.")
            elif guess > number:
                print("📈 Too high! Try again.")
            else:
                print(f"🎉 Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("⚠️ Please enter a valid number.")

# Run the game
guessing_game()
