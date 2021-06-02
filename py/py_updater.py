from py_data import file_names, iters
import glob
import sys
import io
import os
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))
#try:
#    sys.path.remove(str(parent))
#except ValueError:
#    pass


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
    def conv():
        prefix_dict = {0: 'ns', 1: 'μs', 2: 'ms', 3: ' s'}
        copied, counter = result_avg, 0
        while len(str(int(copied))) > 6:
            copied *= 0.001
            counter += 1
        return f'{result_avg:11,.0f} ' if counter == 0 else f'{copied:9,.0f}' + prefix_dict[counter] + ' '

    def pos_finder(line, option):
        found = 0
        for i, c in enumerate(line):
            if c == '|':
                found += 1
            if c == '|' and found == 2:
                pos_before = i + 1
            if c == '|' and found == 3:
                pos_after = i
                if option == 'before': return pos_before
                if option == 'after': return pos_after
    
    def line_finder(md_dump, option):
        target_a = 'unless specified) (lower is better)'
        target_i = 'Number of Iterations ('
        for i, line in enumerate(md_dump):
            if target_a in line: head_avg = i
            if target_i in line: head_iter = i
        if option == 'avg': 
            for i in range(head_avg, head_iter):
                if md_dump[i].startswith('| ' + str(n) + ' '):
                    return i
            return 0
        if option == 'iter':
            for i in range(head_iter, len(md_dump)):
                if md_dump[i].startswith('| ' + str(n) + ' '):
                    return i
            return 0

    with io.open(get_readme_path(), 'r', encoding='utf-8') as f:
        tmp = f.readlines()
    l_no_avg, l_no_iter = line_finder(tmp, 'avg'), line_finder(tmp, 'iter')
    if l_no_iter != 0 and l_no_avg != 0:
        tmp[l_no_avg] = (
            tmp[l_no_avg][:pos_finder(tmp[l_no_avg], 'before')]
            + '[' + conv() + ']'
            + '(https://github.com/lcsm29/project-euler/blob/main/py/'
            + file_names[n] + '.py)'
            + tmp[l_no_avg][pos_finder(tmp[l_no_avg], 'after'):]
        )
        tmp[l_no_iter] = (
            tmp[l_no_iter][:pos_finder(tmp[l_no_iter], 'before')]
             + f'{iters[n]:11,.0f} '
             + tmp[l_no_iter][pos_finder(tmp[l_no_iter], 'after'):]
        )
        with io.open(get_readme_path(), 'w', encoding='utf-8') as f:
            f.writelines(tmp)
