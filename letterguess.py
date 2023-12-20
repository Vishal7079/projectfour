
import random

def hangman():
    words = ["apple", "banana", "cherry", "orange", "watermelon"]  # List of words to choose from
    word = random.choice(words)  # Select a random word from the list
    guessed_letters = []
    tries = 6  # Number of tries the player has

    while tries > 0:
        # Display the current state of the word
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"
        print(display_word)

        # Get a letter guess from the player
        guess = input("Guess a letter: ").lower()

        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You've already guessed that letter. Try again!")
            continue

        # Add the letter to the list of guessed letters
        guessed_letters.append(guess)

        # Check if the letter is in the word
        if guess in word:
            print("Correct guess!")
        else:
            print("Wrong guess!")
            tries -= 1

        # Check if the player has guessed all the letters
        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You guessed the word:", word)
            break

    if tries == 0:
        print("Game over! The word was:", word)

# Start the game
hangman()
