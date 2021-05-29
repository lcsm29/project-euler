# Solution of;
# Project Euler Problem 686: Powers of Two
# https://projecteuler.net/problem=686
# 
# $2^7=128$ is the first power of two whose leading digits are "12". The next 
# power of two whose leading digits are "12" is $2^{80}$. Define $p(L, n)$ to 
# be the $n$th-smallest value of $j$ such that the base 10 representation of 
# $2^j$ begins with the digits of $L$. So $p(12, 1) = 7$ and $p(12, 2) = 80$. 
# You are also given that $p(123, 45) = 12710$. Find $p(123, 678910)$.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 686
    timed.caller(dummy, n, i, prob_id)
