# Root Crawl

A text-based dungeon crawler that runs in your terminal. Folders are rooms, files are enemies, and you fight your way through the directory tree.

> **Work in progress.** Exploring rooms works, combat is still being built.

## How it works

- Every **folder** is a room, and its subfolders are the exits.
- Every **file** in a room is an enemy.
- The game only **reads** your file system. Nothing is ever deleted, moved or changed. "Defeating" a file only happens inside the game.

## Requirements

- Python 3.10 or newer (the game uses `match` statements)
- No extra packages needed

## Run it

```bash
git clone https://github.com/TheRealStar1/root-crawl.git
cd root-crawl
python main.py
```

The game starts in the included `test_dungeon` folder, so you can try it out safely.

## Commands

| Command | What it does |
| --- | --- |
| `go <exit>` | Enter a neighbouring room, e.g. `go raum2` |
| `attack <enemy>` | Attack an enemy in the current room, e.g. `attack gegner1.txt` |

## Roadmap

- [x] Rooms and exits built from real folders
- [x] Moving between rooms
- [ ] `back` command to leave a room
- [ ] Turn-based combat (file size = health, file type = enemy type)
- [ ] Loot, inventory and levels
- [ ] Boss per room (largest file)
- [ ] Save games and a room map
- [ ] Load rooms only when entered, so large folders work

## Known limitations

The whole folder tree is loaded at start. Keep to `test_dungeon` or other small folders for now, because huge folders (like a whole drive) will be slow or hit locked directories.

## License

MIT, see [LICENSE](LICENSE).
