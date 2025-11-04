import random

def main():
    def setup_player():
        """
        Prompts the user to create their player profile.
        """
        user = input("Enter your name: ")

        user_stats = {
            "name": user,
            "health": 10,
            "inventory": []
        }
        return user_stats


    def create_treasures():
        """
        Creates a dictionary of treasures, where each treasure has a random value.
        """
        treasures = {
            "gold coin": random.randint(3, 12),
            "ruby": random.randint(3, 12),
            "ancient scroll": random.randint(3, 12),
            "emerald": random.randint(3, 12),
            "silver ring": random.randint(3, 12)
        }
        return treasures


    def display_options(room_number):
        """
        Displays available options for the player in the current room.
        """
        print(f"\nYou are in room {room_number}.")
        print("What would you like to do?")
        print("1. Search for treasure")
        print("2. Move to next room")
        print("3. Check health and inventory")
        print("4. Quit the game")


    def search_room(player, treasures):
        """
        Simulates searching the current room for treasure or trap.
        """
        outcome = random.choice(["treasure", "trap"])

        if outcome == "treasure":
            item = random.choice(list(treasures.keys()))
            player["inventory"].append(item)
            print(f"You found a {item}! It’s added to your inventory.")
        else:
            player["health"] -= 2
            print("Oh no! You triggered a trap and lost 2 health points!")


    def check_status(player):
        """
        Displays the player’s current health and inventory.
        """
        print(f"\nHealth: {player['health']}")
        if player["inventory"]:
            print("Inventory:", ", ".join(player["inventory"]))
        else:
            print("Inventory: You have no items yet.")


    def end_game(player, treasures):
        """
        Ends the game and displays a summary.
        """
        total_value = sum(treasures[item] for item in player["inventory"] if item in treasures)
        print("\n----- GAME OVER -----")
        print(f"Final Health: {player['health']}")
        if player["inventory"]:
            print("Final Inventory:", ", ".join(player["inventory"]))
        else:
            print("You didn’t collect any treasures.")
        print(f"Total Treasure Value: {total_value}")
        print("Thanks for playing!")


    def run_game_loop(player, treasures):
        """
        Main game loop that manages the rooms and player decisions.
        """
        for room in range(1, 6):
            while True:
                if player["health"] < 1:
                    print("\nYou’ve run out of health!")
                    end_game(player, treasures)
                    return

                display_options(room)
                choice = input("Enter your choice (1-4): ")

                if choice == "1":
                    search_room(player, treasures)
                elif choice == "2":
                    print("You move to the next room.")
                    break
                elif choice == "3":
                    check_status(player)
                elif choice == "4":
                    print("You chose to quit.")
                    end_game(player, treasures)
                    return
                else:
                    print("Invalid choice. Try again.")

        # After all rooms are explored
        end_game(player, treasures)


    # -----------------------------------------------------
    # GAME ENTRY POINT (Leave this section unchanged)
    # -----------------------------------------------------
    player = setup_player()
    treasures = create_treasures()
    run_game_loop(player, treasures)


if __name__ == "__main__":
    main()
