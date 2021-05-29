from py_data import file_names
import glob
import sys
import io
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


def py_folder_updater():
    start = 1
    stop = 747
    headers = [str(file.parents[0]) + '\py_' + str(f).zfill(4)
                for f in range(start, stop + 1)]
    for head in headers:
        for filename in glob.glob(head + '*.py'):
            with io.open(filename, 'r', encoding='utf-8') as f:
                tmp = f.readlines()
            if len(tmp) > 3:
                tmp = tmp[:-1]
                tmp.append('    timed.caller(dummy, n, i, prob_id)\n')
                with open(filename, 'w', encoding='utf-8') as f:
                    f.writelines(tmp)


def get_file_names():
    start = 1
    stop = 747
    headers = [str(file.parents[0]) + '\py_' + str(f).zfill(4)
                for f in range(start, stop + 1)]
    file_names = [f.replace(str(file.parents[0]) + '\\', '').replace('.py', '') for head in headers for f in glob.glob(head + '*')]
    for n in file_names:
        name = '#    ' + n.replace('py_', '').strip('0').split('_', 1)[0] + ": '" + n + "',"
        with io.open('py_file_names.txt', 'a', encoding='utf=8') as f:
            f.writelines(name + '\n')
