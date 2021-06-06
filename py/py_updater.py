from py_data import file_names, iters, pypy_iters
import glob
import sys
import os
import io
import platform
import subprocess
import re
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
            tmp[i] = '{} {:6} / 747      |\n'.format(target, len(file_names.keys()))
    with open(get_readme_path(), 'w') as md:
        md.writelines(tmp)


def scoreboard_updater(n, result_avg, target_col='py'):
    def conv():
        prefix_dict = {0: 'ns', 1: 'μs', 2: 'ms', 3: ' s'}
        copied, counter = result_avg, 0
        while len(str(int(copied))) > 6:
            copied *= 0.001
            counter += 1
        return f'{result_avg:11,.0f} ' if counter == 0 else f'{copied:9,.0f}' + prefix_dict[counter] + ' '

    def pos_finder(line, option):
        found = 0
        if target_col == 'py':
            target = 2
        if target_col == 'pypy':
            target = 3
        for i, c in enumerate(line):
            if c == '|':
                found += 1
            if c == '|' and found == target:
                pos_before = i + 1
            if c == '|' and found == target + 1:
                pos_after = i
                if option == 'before': return pos_before
                if option == 'after': return pos_after    

    with io.open(get_readme_path(), 'r', encoding='utf-8') as f:
        tmp = f.readlines()
    l_no_avg = line_finder(tmp, n, 'avg')
    l_no_iter = line_finder(tmp, n, 'iter')
    if l_no_iter != 0 and l_no_avg != 0:
        num_iterations = f'{iters[n]:11,.0f} '
        if target_col == 'pypy':
            num_iterations = f'{pypy_iters[n]:11,.0f} '
        tmp[l_no_avg] = (
            tmp[l_no_avg][:pos_finder(tmp[l_no_avg], 'before')]
            + '[' + conv() + ']'
            + '(https://github.com/lcsm29/project-euler/blob/main/py/'
            + file_names[n] + '.py)'
            + tmp[l_no_avg][pos_finder(tmp[l_no_avg], 'after'):]
        )
        tmp[l_no_iter] = (
            tmp[l_no_iter][:pos_finder(tmp[l_no_iter], 'before')]
             + num_iterations
             + tmp[l_no_iter][pos_finder(tmp[l_no_iter], 'after'):]
        )

        with io.open(get_readme_path(), 'w', encoding='utf-8') as f:
            f.writelines(tmp)
    if l_no_avg == 0 and l_no_iter == 0:
        last_avg = line_finder(tmp, n, 'avg', True)
        new = tmp[:last_avg + 1] + [tmp[last_avg]] + tmp[last_avg + 1:]
        if int(tmp[last_avg][2:8]) < n:
            new[last_avg + 1] = (
                '| ' + str(n).ljust(10, ' ') + '|'
                + '[' + conv() + ']'
                + '(https://github.com/lcsm29/project-euler/blob/main/py/'
                + file_names[n] + '.py)'
                + new[last_avg][pos_finder(new[last_avg], 'after'):]
            )
        last_iter = line_finder(new, n, 'iter', True)
        if int(new[last_iter][2:8]) < n:
            new = new[:last_iter + 1] + [new[last_iter]] + new[last_iter + 1:]
            new[last_iter + 1] = (
                '| ' + str(n).ljust(10, ' ') + '|'
                + f'{iters[n]:11,.0f} '
                + new[last_iter][pos_finder(new[last_iter], 'after'):]
            )
        with io.open(get_readme_path(), 'w', encoding='utf-8') as f:
            f.writelines(new)


def line_finder(md_dump, num_id, option, eot=False):
    target_a = 'unless specified) (lower is better)'
    target_i = 'Number of Iterations ('
    for i, line in enumerate(md_dump):
        if target_a in line: head_avg = i
        if target_i in line: head_iter = i
    if option in ('avg', 'sysinfo'):
        target_line = 0
        for i in range(head_avg, head_iter):
            if md_dump[i].startswith('| ' + str(num_id) + ' '):
                target_line = i
            if md_dump[i].startswith('  * py: '):
                target_sysinfo = i
            if md_dump[i].startswith('* The table ab') and eot:
                target_line = i - 1
        return target_line if option == 'avg' else target_sysinfo
    if option == 'iter' and eot == False:
        for i in range(head_iter, len(md_dump)):
            if md_dump[i].startswith('| ' + str(num_id) + ' '):
                return i
        return 0
    if option == 'iter' and eot:
        for i in range(head_iter, len(md_dump)):
            if md_dump[i].startswith('* Each main script not just'):
                return i - 1


def sysinfo_updater(target_row='py'):
    def get_sys_name(option = 'processor'):
        if platform.system() == 'Linux':
            command = 'cat /proc/cpuinfo'
            all_info = str(subprocess.check_output(command, shell=True))
            for line in all_info.split('\\n'):
                if 'model name' in line:
                    proc_name = re.sub('.*model name.*:', '', line, 1)
            os_name = (
                platform.system() + ' ' 
                + platform.release() + ' ' 
                + '(' + platform.machine() + ')')
        if platform.system() == 'Darwin':
            command = 'sysctl -n machdep.cpu.brand_string'
            proc_name = str(subprocess.check_output(command, shell=True))[2:-3]
            os_name = (
                'macOS' + ' '
                + platform.mac_ver()[0] + ' '
                + '(' + platform.machine() + ')')
        if platform.system() == 'Windows':
            proc_name = platform.processor()
            if target_row == 'py':
                os_name = (
                    platform.system() + ' ' 
                    + platform.release() + ' ' 
                    + platform.win32_edition() + ' '
                    + '(' + platform.machine() + ')')
            if target_row == 'pypy':
                os_name = (
                    platform.system() + ' ' 
                    + platform.release() + ' ' 
                    + '(' + platform.machine() + ')')
        return proc_name if option == 'processor' else os_name

    print('Writing system info to README.md...')
    with io.open(get_readme_path(), 'r', encoding='utf-8') as f:
        tmp = f.readlines()
    l_sysinfo = line_finder(tmp, 1, 'sysinfo')
    if target_row == 'pypy':
        l_sysinfo += 1
    oname = get_sys_name('os')
    ver = 'Python ' + platform.python_version()
    if target_row == 'pypy':
        ver = sys.version.split('\n')[1].strip('[]')
    try:
        import cpuinfo
        cpu_nf = cpuinfo.get_cpu_info()
        ver = 'Python ' + cpu_nf['python_version']
        cpu = cpu_nf['brand_raw']
    except (ModuleNotFoundError, AttributeError):
        cpu = get_sys_name('processor')
    tmp[l_sysinfo] = f'  * {target_row}: ' + ver + ', ' + oname + ', ' + cpu + '\n'
    with io.open(get_readme_path(), 'w', encoding='utf-8') as f:
        f.writelines(tmp)
