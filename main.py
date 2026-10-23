from pathlib import Path


pfad = Path("root-crawl/test_dungeon")



def read_folder(path):
   global pfad
   for element in path.iterdir():
      if element.is_dir():
        pfad = pfad / f"{element.name}"
        read_folder(pfad)
      elif element.is_file():
        print(f"[DATEI]  {element.name}")


read_folder(pfad)