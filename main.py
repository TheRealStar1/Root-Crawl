from pathlib import Path

running = True

PATH = Path("root-crawl/test_dungeon")
DIR_LVL = 1

current_player_room = PATH


def tree(path):
   global DIR_LVL
   print("|" * DIR_LVL, path)
   for element in path.iterdir():
      if element.is_dir():
        path = path / f"{element.name}"
        DIR_LVL +=1
        tree(path)
      elif element.is_file():
        print("|" * DIR_LVL, "-", f"[DATEI]  {element.name}")

def go_room(room):
   current_player_room = room
   return read_folder(current_player_room)

def read_folder():
   pass

while running:
   player_command = input("What to do next:")
   player_command = player_command.split()
   match player_command[0]:
      case "go":
         print("gehe")