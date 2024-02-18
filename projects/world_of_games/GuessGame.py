import random


def generate_number(difficulty):
    secret_number = random.randint(1, difficulty)
    return secret_number


def get_guess_from_user(difficulty):
    guessed_number = int(input(f"Make a guess between 1 to {difficulty}: "))
    return guessed_number


def compare_results(guessed_number, secret_number):
    if guessed_number == secret_number:
        return True

    return False


def play(difficulty):
    secret_number = generate_number(difficulty)
    guess = get_guess_from_user(difficulty)
    return compare_results(guess, secret_number)
