from GuessGame import play


def welcome(name: str):
    welcome_message = f"Hello <{name}> and welcome to the World of Games (WoG).\n" \
                      f"Here you can find many cool games to play."
    return welcome_message


def load_game():
    message_instruction = (
        "Please choose a game to play: \n\t\t\t\t1. Guess Game - guess a number and see if you chose like the computer"
        "\n\t\t\t\t2. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back"
        "\n\t\t\t\t3. Currency Roulette - try and guess the value of a random amount of USD in ILS): ")

    game_difficulty_message = "Please choose game difficulty from 1 to 10:"

    game_number = input(message_instruction)
    while game_number != '1' and game_number != '2' and game_number != '3':
        game_number = input("please enter valid game number from 1 to 3: ")

    game_difficulty = input(game_difficulty_message)
    while game_difficulty not in {'1', '2', '3', '4', '5', '6', '7', '8', '9', '10'}:
        game_difficulty = input("please enter valid game difficulty from 1 to 10: ")

    game_user_choice = int(game_number)
    difficulty_user_choice = int(game_difficulty)

    print(f"You picked game number: {game_user_choice} , difficulty level: {difficulty_user_choice}.")

    if (game_user_choice == 1):

        # run the Guess game with the user difficulty level
        game_result = play(difficulty_user_choice)
        if (game_result):
            print(f"The user guess and won the game :) ")
        else:
            print(f"The user didn't guess and lost the game :( ")
    else:
        print("only [Guess Game] is implemented!")


# load the main game
load_game()
