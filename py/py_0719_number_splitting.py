# Solution of;
# Project Euler Problem 719: Number Splitting
# https://projecteuler.net/problem=719
# 
# We define an $S$-number to be a natural number, $n$, that is a perfect 
# square and its square root can be obtained by splitting the decimal 
# representation of $n$ into 2 or more numbers then adding the numbers. For 
# example, 81 is an $S$-number because $\sqrt{81} = 8+1$. 6724 is an 
# $S$-number: $\sqrt{6724} = 6+72+4$. 8281 is an $S$-number: $\sqrt{8281} = 
# 8+2+81 = 82+8+1$. 9801 is an $S$-number: $\sqrt{9801}=98+0+1$. Further we 
# define $T(N)$ to be the sum of all $S$ numbers $n\le N$. You are given 
# $T(10^4) = 41333$. Find $T(10^{12})$
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 719
    timed.caller(dummy, n, i, prob_id)
