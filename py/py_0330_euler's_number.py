# Solution of;
# Project Euler Problem 330: Euler's Number
# https://projecteuler.net/problem=330
# 
# An infinite sequence of real numbers a(n) is defined for all integers n as 
# follows:$$a(n) = \begin{cases}1 & n \lt 0\\\sum \limits_{i = 
# 1}^{\infty}{\dfrac{a(n - i)}{i!}} & n \ge 0\end{cases}$$For example,$a(0) = 
# \dfrac{1}{1!} + \dfrac{1}{2!} + \dfrac{1}{3!} + \cdots = e - 1$$a(1) = 
# \dfrac{e - 1}{1!} + \dfrac{1}{2!} + \dfrac{1}{3!} + \cdots = 2e - 3$$a(2) = 
# \dfrac{2e - 3}{1!} + \dfrac{e - 1}{2!} + \dfrac{1}{3!} + \cdots = 
# \dfrac{7}{2}e - 6$with $e = 2. 7182818. . . $ being Euler's constant. It can 
# be shown that $a(n)$ is of the form $\dfrac{A(n)e + B(n)}{n!}$ for integers 
# $A(n)$ and $B(n)$. For example, $a(10) = \dfrac{328161643e - 
# 652694486}{10!}$. Find $A(10^9) + B(10^9)$ and give your answer mod 77 777 
# 777.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 330
    timed.caller(dummy, n, i, prob_id)
