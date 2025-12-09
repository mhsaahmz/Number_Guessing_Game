import random

print('''
Welcome to the number-guessing game!
Please guess a number between 1 and 1000.
(Type "exit" to quit)
''')

target_number = random.randint(1, 1000)
counter = 0

while True:
    guess = input('Enter your guess: ')

    # Allow user to exit
    if guess.lower() == "exit":
        print("Game exited.")
        break

    # Validate input
    if not guess.isdigit():
        print("Please enter a valid number!")
        continue

    guess_number = int(guess)

    # Validate range
    if guess_number < 1 or guess_number > 1000:
        print("Please enter a number between 1 and 1000!")
        continue

    counter += 1

    if guess_number < target_number:
        print("Guess a larger number:")
    elif guess_number > target_number:
        print("Guess a smaller number:")
    else:
        print("Well done! You won!")
        print("Number of guesses:", counter)
        break
