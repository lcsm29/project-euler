# Solution of;
# Project Euler Problem 372: Pencils of rays
# https://projecteuler.net/problem=372
# 
# Let $R(M, N)$ be the number of lattice points $(x, y)$ which satisfy 
# $M\!\lt\!x\!\le\!N$, $M\!\lt\!y\!\le\!N$ and 
# $\large\left\lfloor\!\frac{y^2}{x^2}\!\right\rfloor$ is odd. We can verify 
# that $R(0, 100) = 3019$ and $R(100, 10000) = 29750422$. Find $R(2\cdot10^6, 
# 10^9)$. Note: $\lfloor x\rfloor$ represents the floor function.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
