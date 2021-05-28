import statistics as stat
import time


def caller(fn, feed_var, num_iterations):
    str_fn = str(fn)[10:str(fn).index(' at ')] + '()'
    r = []
    outer = time.perf_counter_ns()
    for _ in range(num_iterations):
        start = time.perf_counter_ns()
        fn(feed_var)
        r.append(time.perf_counter_ns() - start)
    print(f"time elapsed {str_fn}: {time.perf_counter_ns() - outer:,}ns "
            f"(min: {min(r):,}ns, mean: {stat.mean(r):,}ns, max: {max(r):,}ns)")
    return {str_fn: (min(r), stat.mean(r), max(r))}
