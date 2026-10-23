from pathlib import Path
import os

running = True

PATH = Path(__file__).parent / "test_dungeon"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

class Enemy:
    def __init__(self, name, path):
        self.name = name
        self.path = path
        self.file_size = os.path.getsize(self.path)
        self.health = self.file_size * 0.1
        self.typ = None

class Room:
    def __init__(self, path, parent=None, name=None):
        self.path = path
        self.parent = parent
        self.name = name
        self.exits = {}      # Name des Unterordners -> Room
        self.enemies = {}    # Dateiname -> Enemy
        self.build_rooms()

    def build_rooms(self):
        for element in self.path.iterdir():
            if element.is_dir():
                self.exits[element.name] = Room(element, parent=self, name=element.name)
            elif element.is_file():
                self.enemies[element.name] = Enemy(element.name, element)

    def draw_room(self):
        for name in self.exits:
            print(f"[Exit]  {name}")
        for name in self.enemies:
            print(f"[Enemy]  {name} HP: {self.enemies[name].health}")

current_player_room = Room(PATH, name="test_dungeon")

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
                print(f"Entered {player_command[1]}:")
            else:
                print("That is not a valid exit.")
        case "attack":
            if len(player_command) > 1 and player_command[1] in current_player_room.enemies:
                print(f"Attacking {current_player_room.enemies[player_command[1]].name}")
            else:
                print("That is not a valid attack.")
        case "back":
            if current_player_room.parent:
                current_player_room = current_player_room.parent
                clear()
                print(f"Entered {current_player_room.name}")
        case _:
            print("That is not a valid command.")