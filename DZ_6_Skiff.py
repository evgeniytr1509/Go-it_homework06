from pathlib import Path
import shutil
import sys


CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u","f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
TRANS = {}

for cir, lat in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        TRANS[ord(cir)]=lat
        TRANS[ord(cir.upper())]=lat.upper()

def normalise(text):
        return text.translate(TRANS)

SORTING_DICT = {'picture':['.jpg', '.bmp', '.jpg', '.png'],
                'video':['.avi', '.mp4', '.wmv', '.3gpp'],
                'documents':['.doc', '.docx', '.xls', '.xlsx' '.txt', '.pdf', '.pptx'],
                'music':['.mp3', '.wav', '.flac', '.aac', 'ogg', 'amr'],
                'archives':['.zip', '.rar', 'gz', 'tar'],
                'other': []}


def get_category(file:Path):
    extensions = file.suffix.lower()
    for cat, exts in SORTING_DICT.items():
        if extensions in exts:
            return cat
    return 'other'


def move_file(file:Path, root:Path, category:str):
    target_folder = root / category
    if not target_folder.exists():
        target_folder.mkdir()
    return file.replace(target_folder / f"{normalise(file.stem)}{file.suffix}")


def sort_folder(path:Path, target_path:Path):
    
    for item in [p for p in path.glob("*") if p.name not in SORTING_DICT.keys()]:
        if item.is_dir():
            sort_folder(item, target_path)
            item.rmdir()
        else:
            category = get_category(item)
            new_place = move_file(item, target_path, category)
            if category == 'archives':
                shutil.unpack_archive(new_place, new_place.parent / new_place.stem)
    

def main():
    try:
        path = Path(sys.argv[1])
    except IndexError:
        print("Sorry, take a path as a parameter")
        return None
    
    if not path.exists():
        print(f"Path {path} not exists")
        return None
    
    sort_folder(path, path)


if __name__ == "__main__":
    main()