# /usr/bin/env python3
"""
Mastermind
"""

from random import randint

# I know global variables are frowned upon, but it's neater this way for now.
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
attempts = 0
difficulty = 0
computer_guesses = []
player_guesses = []
game_over = False


def player_round(difficulty):
    """
    Creates a loop to store player guesses.
    Returns a list of guesses
    """
    guess_list = []
    for x in range(difficulty):
        guess = input(f"Enter Guess No. {x+1}: ")
        if guess not in colors:
            print("Your guess do not belong to the color choices. Try again.")
            guess = input(f"Enter Guess No. {x+1}: ")
        guess_list.append(guess.lower())
    return guess_list


def evaluate_guesses(computer_guesses, player_guesses):
    """
    Evaluates the player's answers to the computer's answers.
    Returns true if the player figured it out.
    Returns false if the player has not figured it out.
    """
    # call global attempts
    global attempts
    attempts = attempts + 1

    # Store correct guesses
    right_color_place = 0
    right_color_wrong_place = 0

    # Check if the player's guesses match the computer's guess.
    if computer_guesses == player_guesses:
        return True

    # Check how many guesses the player got right and in what way
    for index, value in enumerate(player_guesses):
        if player_guesses[index] == computer_guesses[index]:
            right_color_place = right_color_place + 1
        elif player_guesses[index] in computer_guesses:
            right_color_wrong_place = right_color_wrong_place + 1

    # Tell the player what they got right
    print("You haven't got it right just yet.")
    print(f"Correct color in the correct place: {right_color_place}")
    print(f"Correct color but in the wrong place: {right_color_wrong_place}")
    print("Try again.")
    return False


def main():

    # Introduction of the Game
    print(
        "\nWelcome to the Mastermind Game\n\n\
Your task is to read the mind of the Master\n\
and correctly guess his chosen colors in the\n\
right order."
    )

    print(f"Here are the colors you'll be choosing:\n{colors}.\n\n")
    global difficulty
    difficulty = int(input("Choose your difficulty (4-7): "))
    if difficulty not in range(4, 8):
        print("Try again.")
        difficulty = int("Choose your difficulty (4-7): ")

    # The Computer makes his guesses
    global computer_guesses
    for x in range(difficulty):
        computer_guesses.append(colors[randint(0, difficulty)])
    print("\n\nComputer has made his guesses.\nGame start.\n")

    # The game loop begins
    global game_over
    while not game_over:
        # The Player attempts a guess
        global player_guesses
        player_guesses = player_round(difficulty)

        # The answers are evaluated.
        game_over = evaluate_guesses(computer_guesses, player_guesses)

    print("Congratulations. You got it right.")
    print(f"The computer's choices were {computer_guesses}.")
    print(f"You got it in {attempts} attempts.")
    print("Thank you for playing.")


# Run the game
main()
