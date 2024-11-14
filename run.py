from game import RPGYnov
from save import load_game

def start_menu():
    print("===== RPG GAME =====")
    print("1. Start New Game")
    print("2. Load Game")
    print("3. Quit")

    choice = input("Choose an option: ")
    return choice

def main():
    while True:
        choice = start_menu()
        if choice == "1":
            # Start a new game
            game = RPGYnov()
            game.run()
        elif choice == "2":
            # Load a saved game
            player, game_map = load_game()
            if player and game_map:
                game = RPGYnov(map_w=game_map.width, map_h=game_map.height)
                game.player = player  # Restore the player's state
                game.game_map = game_map  # Restore the map
                game.run()
            else:
                print("Failed to load the game.")
        elif choice == "3":
            print("Exiting game. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
