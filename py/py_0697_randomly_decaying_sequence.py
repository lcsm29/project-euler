# Solution of;
# Project Euler Problem 697: Randomly Decaying Sequence
# https://projecteuler.net/problem=697
# 
# Given a fixed real number $c$, define a random sequence $(X_n)_{n\ge 0}$ by 
# the following random process:$X_0 = c$ (with probability 1). For $n>0$, $X_n 
# = U_n X_{n-1}$ where $U_n$ is a real number chosen at random between zero 
# and one, uniformly, and independently of all previous choices $(U_m)_{m<n}$. 
# If we desire there to be precisely a 25% probability that $X_{100}<1$, then 
# this can be arranged by fixing $c$ such that $\log_{10} c \approx 46. 27$. 
# Suppose now that $c$ is set to a different value, so that there is precisely 
# a 25% probability that $X_{10\,000\,000}<1$. Find $\log_{10} c$ and give 
# your answer rounded to two places after the decimal point.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 697
    timed.caller(dummy, n, i, prob_id)
