# Solution of;
# Project Euler Problem 741: Binary grid colouring
# https://projecteuler.net/problem=741
# 
# Let $f(n)$ be the number of ways an $n\times n$ square grid can be coloured, 
# each cell either black or white, such that each row and each column contains 
# exactly two black cells. For example, $f(4)=90$, $f(7) = 3110940$ and $f(8) 
# = 187530840$. Let $g(n)$ be the number of colourings in $f(n)$ that are 
# unique up to rotations and reflections. You are given $g(4)=20$, $g(7) = 
# 390816$ and $g(8) = 23462347$ giving $g(7)+g(8) = 23853163$. Find $g(7^7) + 
# g(8^8)$. Give your answer modulo $1\,000\,000\,007$.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 741
    timed.caller(dummy, n, i, prob_id)
