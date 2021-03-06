# Solution of;
# Project Euler Problem 627: Counting products
# https://projecteuler.net/problem=627
# 
# Consider the set $S$ of all possible products of $n$ positive integers not 
# exceeding $m$, that is $S=\{ x_1x_2\dots x_n \, | \, 1 \le x_1, x_2, . . . , 
# x_n \le m \}$. Let $F(m,n)$ be the number of the distinct elements of the 
# set $S$. For example, $F(9, 2) = 36$ and $F(30,2)=308$. Find $F(30, 
# 10001)\text{ mod }1\,000\,000\,007$.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 627
    timed.caller(dummy, n, i, prob_id)
