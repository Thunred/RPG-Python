import pickle

# Function to save the game state
def save_game(player, game_map, filename="savegame.sav"):
    with open(filename, "wb") as f:
        # Save the player's state and map
        pickle.dump({'player': player, 'game_map': game_map}, f)
    print("Game saved successfully!")

# Function to load the game state
def load_game(filename="savegame.sav"):
    try:
        with open(filename, "rb") as f:
            saved_data = pickle.load(f)
            player = saved_data['player']
            game_map = saved_data['game_map']
            print("Game loaded successfully!")
            return player, game_map
    except FileNotFoundError:
        print("No saved game found.")
        return None, None
