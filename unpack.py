import zipfile
from pathlib import Path
def conddel(path):
    if path.exists():
        path.unlink()
conddel(Path("decoded/project.json"))
Path("decoded").rmdir()
zipfile.ZipFile("root.llsp3", "r").extract("scratch.sb3", path="decoded")
zipfile.ZipFile("decoded/scratch.sb3", "r").extract("project.json", path="decoded")
Path("decoded/scratch.sb3").unlink()
