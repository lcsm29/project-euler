# Solution of;
# Project Euler Problem 546: The Floor's Revenge
# https://projecteuler.net/problem=546
# 
# Define fk(n) = $\sum_{i=0}^{n}$ fk($\lfloor\frac{i}{k}\rfloor$) where fk(0) 
# = 1 and $\lfloor x \rfloor$ denotes the floor function. For example, f5(10) 
# = 18, f7(100) = 1003, and f2(103) = 264830889564. Find $(\sum_{k=2}^{10}$ 
# fk(1014)$)$ mod (109+7).
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 546
    timed.caller(dummy, n, i, prob_id)
