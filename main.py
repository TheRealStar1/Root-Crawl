from pathlib import Path


pfad = Path("root-crawl/test_dungeon")

# Alle Elemente im Ordner durchgehen
for element in pfad.iterdir():
  if element.is_dir():
    pfad = pfad / f"{element.name}"
    print(pfad)
    for e in pfad.iterdir():
        if e.is_dir():
            print(f"[ORDNER]  {e.name}")
        elif e.is_file():
            print(f"[DATEI]  {e.name}")
  elif element.is_file():
    print(f"[DATEI]  {element.name}")
