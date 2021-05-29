# Solution of;
# Project Euler Problem 479: Roots on the Rise
# https://projecteuler.net/problem=479
# 
# Let $a_k$, $b_k$, and $c_k$ represent the three solutions (real or complex 
# numbers) to the equation$\frac 1 x = (\frac k x)^2(k+x^2)-k x$. For 
# instance, for $k=5$, we see that $\{a_5, b_5, c_5 \}$ is approximately $\{5. 
# 727244, -0. 363622+2. 057397i, -0. 363622-2. 057397i\}$. Let $\displaystyle 
# S(n) = \sum_{p=1}^n\sum_{k=1}^n(a_k+b_k)^p(b_k+c_k)^p(c_k+a_k)^p$. 
# Interestingly, $S(n)$ is always an integer. For example, $S(4) = 51160$. 
# Find $S(10^6)$ modulo $1\,000\,000\,007$.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 479
    timed.caller(dummy, n, i, prob_id)
