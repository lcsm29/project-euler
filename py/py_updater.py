from py_data import file_names
import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))
try:
    sys.path.remove(str(parent))
except ValueError:
    pass

def readme_updater():
    readme_full_path = str(file.parents[1]) + '\README.md'
    target = '| [Python](https://github.com/lcsm29/project-euler/tree/main/py)                 |'
    with open(readme_full_path, 'r') as md:
        tmp = md.readlines()
    for i, line in enumerate(tmp):
        if line.startswith(target):
            tmp[i] = '{} {} / 747           |\n'.format(target, len(file_names.keys()))
    with open(readme_full_path, 'w') as md:
        md.writelines(tmp)
