from pathlib import Path


pfad = Path("root-crawl/test_dungeon")


ebene = 1
def read_folder(path):
   global pfad, ebene
   print("|" * ebene, pfad)
   for element in path.iterdir():
      if element.is_dir():
        pfad = pfad / f"{element.name}"
        ebene +=1
        read_folder(pfad)
      elif element.is_file():
        print("|" * ebene, "-", f"[DATEI]  {element.name}")


read_folder(pfad)