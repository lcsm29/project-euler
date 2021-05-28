# Solution of;
# Project Euler Problem 137: Fibonacci golden nuggets
# https://projecteuler.net/problem=137
# 
# Consider the infinite polynomial series $A_F(x) = x F_1 + x^2 F_2 + x^3 F_3 
# + \dots$, where $F_k$ is the $k$th term in the Fibonacci sequence: $1, 1, 2, 
# 3, 5, 8, \dots$; that is, $F_k = F_{k-1} + F_{k-2}$, $F_1 = 1$ and $F_2 = 
# 1$. For this problem we shall be interested in values of $x$ for which 
# $A_F(x)$ is a positive integer. Surprisingly$\begin{align*} 
# A_F(\tfrac{1}{2}) &= (\tfrac{1}{2})\times 1 + (\tfrac{1}{2})^2\times 1 + 
# (\tfrac{1}{2})^3\times 2 + (\tfrac{1}{2})^4\times 3 + (\tfrac{1}{2})^5\times 
# 5 + \cdots \\ &= \tfrac{1}{2} + \tfrac{1}{4} + \tfrac{2}{8} + \tfrac{3}{16} 
# + \tfrac{5}{32} + \cdots \\ &= 2\end{align*}$The corresponding values of x 
# for the first five natural numbers are shown below. 
# $x$$A_F(x)$$\sqrt{2}-1$1$\tfrac{1}{2}$2$\frac{\sqrt{13}-2}{3}$3$\frac{\sqrt{89}-5}{8}$4$\frac{\sqrt{34}-3}{5}$5We 
# shall call $A_F(x)$ a golden nugget if $x$ is rational, because they become 
# increasingly rarer; for example, the 10th golden nugget is 74049690. Find 
# the 15th golden nugget.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
