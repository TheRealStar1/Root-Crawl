from pathlib import Path
import os

running = True

PATH = Path("root-crawl/test_dungeon")
DIR_LVL = 1

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
        self.exits = {}     # Name des Unterordners -> Room
        self.enemies = {}   # Dateien in diesem Raum
        self.build_rooms()

    def build_rooms(self):
        for element in self.path.iterdir():
            if element.is_dir():
                next_path = self.path / f"{element.name}"
                new_exit = Room(next_path)
                self.exits[element.name] = new_exit
            elif element.is_file():
                new_enemie = Enemy(element.name)
                self.enemies[element.name] = new_enemie

    def draw_room(self):
        for element in self.path.iterdir():
            if element.is_dir():
                print(f"[Exit]  {element.name}")
            elif element.is_file():
                print(f"[Enemy]  {element.name}")

current_player_room = Room(PATH)

while running:
   current_player_room.draw_room()
   player_command = input("What is your next move? ")
   player_command = player_command.split()
   if not player_command:
       continue

   match player_command[0]:
        case "go":
            if len(player_command) > 1 and player_command[1] in current_player_room.exits:
                print("Entering the next room:")
                current_player_room = current_player_room.exits[player_command[1]]
                clear()
            else:
                print("That is not a valid exit.")
        case "attack":
            if len(player_command) > 1 and player_command[1] in current_player_room.enemies:
               print(f"Attacking {current_player_room.enemies[player_command[1]].name}")
            else:
                print("That is not a valid attack.")
        case _:
           print("That is not a valid command.")