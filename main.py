from pathlib import Path

# The Path of the directory to be sorted
p = Path(input("Add a windows path:"))
# This populates a list with the filenames in the directory
fileList = [x for x in p.iterdir() if x.is_file()]

for file_ in fileList:
    cible = file_.parent.joinpath('target')
    cible.mkdir(exist_ok=True)
    target = cible.joinpath(file_.name)
    print(target)
    if target.exists():
        target = target.with_stem(f'{file_.stem}0')
    file_.replace(target)
