from pathlib import Path

running = True

PATH = Path("root-crawl/test_dungeon")
DIR_LVL = 1

class Enemy:
    def __init__(self):
        self.name = ""
        self.health = 100
        self.typ

class Room:
    def __init__(self, path):
        self.path = path
        self.exits = {}     # Name des Unterordners -> Room
        self.enemies = []   # Dateien in diesem Raum
        self.build_rooms()

    def build_rooms(self):
        for element in self.path.iterdir():
            if element.is_dir():
                next_path = self.path / f"{element.name}"
                new_exit = Room(next_path)
                self.exits[element.name] = new_exit
            elif element.is_file():
                self.enemies.append(element)

    def draw_room(self):
        for element in self.path.iterdir():
            if element.is_dir():
                print(f"[Ausgang]  {element.name}")
            elif element.is_file():
                print(f"[Gegner]  {element.name}")

current_player_room = Room(PATH)

while running:
   current_player_room.draw_room()
   player_command = input("Was ist ihr nächster Zug?:")
   player_command = player_command.split()
   match player_command[0]:
        case "gehe":
            if player_command[1] in current_player_room.exits:
                print("Betrete den nächsten Raum:")
                current_player_room = current_player_room.exits[player_command[1]]
            else:
                print("Das ist kein gültiger Ausgang.")
        case _:
           print("Das ist kein gültiger Befehl.")