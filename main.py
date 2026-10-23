from pathlib import Path


PATH = Path("root-crawl/test_dungeon")

DIR_LVL = 1

current_player_room = PATH

def read_folder(path):
   global PATH, DIR_LVL
   print("|" * DIR_LVL, PATH)
   for element in path.iterdir():
      if element.is_dir():
        PATH = PATH / f"{element.name}"
        DIR_LVL +=1
        read_folder(PATH)
      elif element.is_file():
        print("|" * DIR_LVL, "-", f"[DATEI]  {element.name}")

def go_room(room):
   current_player_room = room
   return read_folder(current_player_room)

