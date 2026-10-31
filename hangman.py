import random

WORDS = {
    "python": "A popular programming language",
    "planet": "A large object that orbits a star",
    "guitar": "A musical instrument with strings",
    "library": "A place where you can borrow books",
    "rainbow": "A colorful arc that can appear after rain",
}

HANGMAN_STAGES = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """,
]


def play_game():
    word, hint = random.choice(list(WORDS.items()))
    guessed_letters = set()
    incorrect_guesses = 0
    max_attempts = len(HANGMAN_STAGES) - 1

    print("\nWelcome to Hangman!")
    print(f"Hint: {hint}")

    while incorrect_guesses < max_attempts:
        print(HANGMAN_STAGES[incorrect_guesses])
        print("Word:", " ".join(
            letter if letter in guessed_letters else "_" for letter in word
        ))
        print(f"Incorrect guesses: {incorrect_guesses}/{max_attempts}")
        print("Guessed letters:", " ".join(sorted(guessed_letters)) or "None")

        if all(letter in guessed_letters for letter in word):
            print("\nYou won! The word was:", word)
            return

        guess = input("Guess a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter one letter (A–Z).\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.\n")
            continue

        guessed_letters.add(guess)

        if guess not in word:
            incorrect_guesses += 1
            print("That letter isn't in the word.\n")
        else:
            print("Good guess!\n")

    print(HANGMAN_STAGES[incorrect_guesses])
    print("You lost! The word was:", word)


def main():
    while True:
        play_game()
        play_again = input("\nPlay again? (y/n): ").strip().lower()

        if play_again not in {"y", "yes"}:
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()