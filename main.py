from pathlib import Path
import os, time

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
        self.damage = 20
        self.typ = None
        self.is_alive = True

    def take_damage(self, amount):
        self.health -= amount

        if self.health <= 0:
            self.is_alive = False

class Player:
    def __init__(self, start_room):
        self.current_room = start_room
        self.health = 200
        self.damage = 20
        self.is_alive = True

    def take_damage(self, amount):
                self.health -= amount
                
                if self.health <= 0:
                    self.is_alive = False
    def dead(self):
        print("You are dead.")
        
    def change_room(self, player_command):
        if len(player_command) > 1 and player_command[1] in player.current_room.exits:
            player.current_room = player.current_room.exits[player_command[1]]
            clear()
            print(f"Entered {player_command[1]}:")
        else:
            print("That is not a valid exit.")

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
            if self.enemies[name].is_alive:
                print(f"[Enemy]  {name} HP: {self.enemies[name].health}")


def fight(player, enemy):
    while player.is_alive and enemy.is_alive:
        print(f"Player HP: {player.health} Enemy HP: {enemy.health}")
        enemy.take_damage(player.damage)
        player.take_damage(enemy.damage)
        time.sleep(0.5)
    if enemy.is_alive == False:
        clear()
        print("Defeted Enemy")
    if player.is_alive == False:
        player.dead()


player = Player(Room(PATH, name="test_dungeon"))
player.current_room

if __name__ == "__main__":
    while running:
        player.current_room.draw_room()
        player_command = input("What is your next move? ").split()
        if not player_command:
            continue

        match player_command[0]:
            case "go":
                player.change_room(player_command)
            case "attack":
                if len(player_command) > 1 and player_command[1] in player.current_room.enemies:
                    print(f"Attacking {player.current_room.enemies[player_command[1]].name}")
                    fight(player, player.current_room.enemies[player_command[1]])
                else:
                    print("That is not a valid attack.")
            case "back":
                if player.current_room.parent:
                    player.current_room = player.current_room.parent
                    clear()
                    print(f"Entered {player.current_room.name}")
            case _:
                print("That is not a valid command.")