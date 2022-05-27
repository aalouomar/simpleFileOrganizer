import collections
from pathlib import Path
from pprint import pprint

targetDir = Path(r'D:\Download')
# p = Path(input("Add a windows path:"))
fileList = [x for x in targetDir.rglob('*') if x.is_file() and not x.is_relative_to(targetDir.joinpath('OrganizerPie'))]
dirList = [x for x in targetDir.rglob('*') if x.is_dir() and not x.is_relative_to(targetDir.joinpath('OrganizerPie'))]
pprint(collections.Counter(p.suffix for p in fileList))
targetExt = input('Choose an extesion to sorte:')
distPath = targetDir.joinpath('OrganizerPie', targetExt)
distPath.mkdir(parents=True, exist_ok=True)
for f in fileList:
    if f.suffix == f'.{targetExt}':
        distFilePath = distPath.joinpath(f.name)
        if not distFilePath.exists():
            f.replace(distFilePath)


