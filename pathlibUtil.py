from pathlib import Path
from pprint import pprint

# p = Path(input("Add a windows path:"))
p = Path().cwd()
# pprint([x for x in p.iterdir() if x.is_dir()])
# files = [x for x in p.iterdir() if x.is_file()]
# for file in files:
#     print(file.suffix)


def tree(directory):
    print(f'+ {directory}')
    for path in sorted(directory.rglob('*')):
        depth = len(path.relative_to(directory).parts)
        spacer = '    ' * depth
        if path.is_dir():
            print(f'{spacer}+ {path.name}')


tree(p)
