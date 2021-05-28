# Solution of;
# Project Euler Problem 678: Fermat-like Equations
# https://projecteuler.net/problem=678
# 
# If a triple of positive integers $(a, b, c)$ satisfies $a^2+b^2=c^2$, it is 
# called a Pythagorean triple. No triple $(a, b, c)$ satisfies $a^e+b^e=c^e$ 
# when $e \ge 3$ (Fermat's Last Theorem). However, if the exponents of the 
# left-hand side and right-hand side differ, this is not true. For example, 
# $3^3+6^3=3^5$. Let $a, b, c, e, f$ be all positive integers, $0 \lt a \lt 
# b$, $e \ge 2$, $f \ge 3$ and $c^f \le N$. Let $F(N)$ be the number of $(a, 
# b, c, e, f)$ such that $a^e+b^e=c^f$. You are given $F(10^3) = 7$, $F(10^5) 
# = 53$ and $F(10^7) = 287$. Find $F(10^{18})$.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)