# Solution of;
# Project Euler Problem 715: Sextuplet Norms
# https://projecteuler.net/problem=715
# 
# Let $f(n)$ be the number of $6$-tuples $(x_1,x_2,x_3,x_4,x_5,x_6)$ such 
# that:All $x_i$ are integers with $0 \leq x_i < 
# n$$\gcd(x_1^2+x_2^2+x_3^2+x_4^2+x_5^2+x_6^2,\ n^2)=1$Let $\displaystyle 
# G(n)=\displaystyle\sum_{k=1}^n \frac{f(k)}{k^2\varphi(k)}$where $\varphi(n)$ 
# is Euler's totient function. For example, $G(10)=3053$ and $G(10^5) \equiv 
# 157612967 \pmod{1\,000\,000\,007}$. Find $G(10^{12})\bmod 1\,000\,000\,007$.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 715
    timed.caller(dummy, n, i, prob_id)
