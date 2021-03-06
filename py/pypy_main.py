import statistics as stat
import time
import importlib
from py_data import *
from py_updater import readme_updater, scoreboard_updater, sysinfo_updater


def call_everything(i, *var):
    global num_fn
    fn_lst = [v for f, v in funcs.__dict__.items() if f.startswith('fn_')]
    result = {str(f)[10:str(f).index(' at ')] + '()': 0 for f in fn_lst}
    for f in fn_lst:
        tmp = []
        outer = time.perf_counter_ns()
        for _ in range(i):
            s = time.perf_counter_ns()
            f.__call__(var[0])
            tmp.append(time.perf_counter_ns() - s)
        result[str(f)[10:str(f).index(' at ')] + '()'] = (
            time.perf_counter_ns() - outer,
            min(tmp), stat.mean(tmp), max(tmp)
        )
        num_fn += 1
    return result


def comparo(result, idx):
    fastest = {'overall': [float('inf'), ''], 'min': [float('inf'), ''],
               'avg':     [float('inf'), ''], 'max': [float('inf'), '']}
    slowest = {'overall': [0, ''], 'min': [0, ''],
               'avg':     [0, ''], 'max': [0, '']}
    for func, ns in result.items():
        print(f"{func} time elapsed: {ns[0]:,}ns "
              f"(min {ns[1]:,}ns, avg {ns[2]:,.0f}ns, max {ns[3]:,}ns)")
        for i, key in enumerate(fastest.keys()):
            if min(fastest[key][0], ns[i]) == ns[i]:
                fastest[key] = [ns[i], func]
            if max(slowest[key][0], ns[i]) == ns[i]:
                slowest[key] = [ns[i], func]
    for f, s in zip(fastest.items(), slowest.items()):
        try:
            mult = f' ({s[1][0]/f[1][0]:.2f}x)'
        except ZeroDivisionError:
            mult = ''
        print(f'fastest {f[0]}: {f[1][1]} took {f[1][0]:,.0f}ns')
        print(f'slowest {s[0]}: {s[1][1]} took {s[1][0]:,.0f}ns{mult}')
    scoreboard_updater(idx, fastest['avg'][0], 'pypy')


def validate_result_once(i, *var):
    fn_lst = [v for f, v in funcs.__dict__.items() if f.startswith('fn_')]
    correct_answer = ans[i]
    num_err = 0
    for f in fn_lst:
        if f.__call__(var[0]) != correct_answer:
            num_err += 1
    print(f"Number of wrong answer{'s' if num_err > 1 else ''}: {num_err}\n")
    return num_err


if __name__ == '__main__':
    fastest_overall = {}
    wrong_answers = {}
    num_fn = 0
    second_per_sol = 1
    for i in file_names.keys():
        iters = get_iters(i, second_per_sol, 'pypy')
        print(f'Calculating Project Euler ID {i} ({iters:,} times): ')
        funcs = importlib.import_module(file_names[i], package=None)
        comparo(call_everything(iters, var[i]), i)
        num_wrong = validate_result_once(i, var[i])
        if num_wrong:
            wrong_answers[i] = num_wrong
    if len(wrong_answers):
        for k, v in wrong_answers.items():
            print(f"ID {k}({file_names[k]}): {v} function(s) failed")
    else:
        print(f"0/{num_fn} function failed")
    readme_updater()
    sysinfo_updater('pypy')
