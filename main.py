from pathlib import Path
import os

running = True

PATH = Path(__file__).parent / "test_dungeon"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

class Enemy:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.typ = None

class Room:
    def __init__(self, path):
        self.path = path
        self.exits = {}      # Name des Unterordners -> Room
        self.enemies = {}    # Dateiname -> Enemy
        self.build_rooms()

    def build_rooms(self):
        for element in self.path.iterdir():
            if element.is_dir():
                self.exits[element.name] = Room(element)
            elif element.is_file():
                self.enemies[element.name] = Enemy(element.name)

    def draw_room(self):
        for name in self.exits:
            print(f"[Exit]  {name}")
        for name in self.enemies:
            print(f"[Enemy]  {name}")

current_player_room = Room(PATH)

while running:
    current_player_room.draw_room()
    player_command = input("What is your next move? ").split()
    if not player_command:
        continue

    match player_command[0]:
        case "go":
            if len(player_command) > 1 and player_command[1] in current_player_room.exits:
                current_player_room = current_player_room.exits[player_command[1]]
                clear()
                print(f"Entering {player_command[1]}:")
            else:
                print("That is not a valid exit.")
        case "attack":
            if len(player_command) > 1 and player_command[1] in current_player_room.enemies:
                print(f"Attacking {current_player_room.enemies[player_command[1]].name}")
            else:
                print("That is not a valid attack.")
        case _:
            print("That is not a valid command.")