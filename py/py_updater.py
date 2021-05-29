from py_data import file_names, iters
import glob
import sys
import io
import os
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))
try:
    sys.path.remove(str(parent))
except ValueError:
    pass


def get_headers(start, stop):
    if os.name == 'nt':
        return [str(file.parents[0]) + '\py_' + str(f).zfill(4)
                 for f in range(start, stop + 1)]
    if os.name == 'posix':
        return [str(file.parents[0]) + '/py_' + str(f).zfill(4)
                 for f in range(start, stop + 1)]


def get_readme_path():
    if os.name == 'nt':
        return str(file.parents[1]) + '\README.md'
    if os.name == 'posix':
        return str(file.parents[1]) + '/README.md'  


def txt_file_names():
    headers = get_headers(1, 747)
    if os.name == 'nt':
        file_names = [f.replace(str(file.parents[0]) + '\\', '').replace('.py', '')
                        for head in headers for f in glob.glob(head + '*')]
    if os.name == 'posix':
        file_names = [f.replace(str(file.parents[0]) + '/', '').replace('.py', '')
                for head in headers for f in glob.glob(head + '*')]
    for n in file_names:
        name = '#    ' + n.replace('py_', '').strip('0').split('_', 1)[0] + ": '" + n + "',"
        with io.open('py_file_names.txt', 'a', encoding='utf=8') as f:
            f.writelines(name + '\n')


def py_folder_updater():
    for head in get_headers(1, 747):
        for filename in glob.glob(head + '*.py'):
            with io.open(filename, 'r', encoding='utf-8') as f:
                tmp = f.readlines()
            if len(tmp) > 3:
                tmp = tmp[:-1]
                tmp.append('    timed.caller(dummy, n, i, prob_id)\n')
                with open(filename, 'w', encoding='utf-8') as f:
                    f.writelines(tmp)


def readme_updater():    
    target = '| [Python](https://github.com/lcsm29/project-euler/tree/main/py)                 |'
    with open(get_readme_path(), 'r') as md:
        tmp = md.readlines()
    for i, line in enumerate(tmp):
        if line.startswith(target):
            tmp[i] = '{} {} / 747           |\n'.format(target, len(file_names.keys()))
    with open(get_readme_path(), 'w') as md:
        md.writelines(tmp)


def scoreboard_updater(n, result_avg):
    target_iter, target_avg = 'Number of Iterations (', 'nanoseconds (lower is better)'
    l_no_iter, l_no_avg = 0, 0
    with io.open(get_readme_path(), 'r', encoding='utf-8') as f:
        tmp = f.readlines()
    for i, line in enumerate(tmp):
        if target_iter in line: l_no_iter = i + 3 + n
        if target_avg in line: l_no_avg = i + 3 + n
    if l_no_iter != 0 and l_no_avg != 0:
        tmp[l_no_avg] = tmp[l_no_avg][:13] + f'{result_avg:>11,.0f} ' + tmp[l_no_avg][25:]
        tmp[l_no_iter] = tmp[l_no_iter][:13] + f'{iters[n]:11,.0f} ' + tmp[l_no_iter][25:]
        with io.open(get_readme_path(), 'w', encoding='utf-8') as f:
            f.writelines(tmp)
