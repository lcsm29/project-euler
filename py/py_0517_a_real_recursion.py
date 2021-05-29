# Solution of;
# Project Euler Problem 517: A real recursion
# https://projecteuler.net/problem=517
# 
# For every real number $a \gt 1$ is given the sequence $g_a$ by:$g_{a}(x)=1$ 
# for $x \lt a$$g_{a}(x)=g_{a}(x-1)+g_a(x-a)$ for $x \ge a$$G(n)=g_{\sqrt 
# {n}}(n)$$G(90)=7564511$. Find $\sum G(p)$ for $p$ prime and $10000000 \lt p 
# \lt 10010000$Give your answer modulo 1000000007.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 517
    timed.caller(dummy, n, i, prob_id)
