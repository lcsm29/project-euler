import statistics as stat
import time
import py_data


def caller(fn, feed_var, num_iterations, id):
    str_fn = str(fn)[10:str(fn).index(' at ')] + '()'
    r = []
    outer = time.perf_counter_ns()
    for _ in range(num_iterations):
        start = time.perf_counter_ns()
        fn(feed_var)
        r.append(time.perf_counter_ns() - start)
    print(f"time elapsed {str_fn}: {time.perf_counter_ns() - outer:,}ns "
            f"(min: {min(r):,.0f}ns, mean: {stat.mean(r):,.0f}ns, max: {max(r):,.0f}ns) ", end='')
    if py_data.ans[id] != fn(feed_var):
        print(f"Expected result: {py_data.ans[id]:,}, "
              f"Actual result: {fn(feed_var):,} (incorrect)")
    else:
        print()
    return {str_fn: (min(r), stat.mean(r), max(r))}
