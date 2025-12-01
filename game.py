import random
def game():
    print("WELCOME TO NUMBER GUESSING GAME")
    print("Guess a number between 1 and 100")

    number= random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    while attempts < max_attempts:
        guess = input("Enter your guess: ")
        try:
            guess = int(guess)
        except ValueError:
            print("Please enter a valid integer.")
            continue

        attempts = attempts+1

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"Congratulations! You've guessed the number {number} in {attempts} attempts.")
            break

    if attempts == max_attempts:
        print(f"Sorry, you've used all your attempts. The number was {number}.")

if __name__ == "__main__":
    game()

