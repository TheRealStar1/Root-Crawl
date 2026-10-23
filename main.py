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

def read_folder(path):
   for element in path.iterdir():
         if element.is_dir():
           print("|" * DIR_LVL, "-", f"[ODNER]  {element.name}")
         elif element.is_file():
           print("|" * DIR_LVL, "-", f"[DATEI]  {element.name}")

while running:
   print(current_player_room)
   read_folder(current_player_room)
   player_command = input("Was ist ihr nächster Zug?:")
   player_command = player_command.split()
   match player_command[0]:
      case "gehe":
        match player_command[1]:
           case "Raum1":
              current_player_room = PATH / "1.raum"
