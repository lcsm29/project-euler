# Solution of;
# Project Euler Problem 680: Yarra Gnisrever
# https://projecteuler.net/problem=680
# 
# Let $N$ and $K$ be two positive integers. $F_n$ is the $n$-th Fibonacci 
# number: $F_1 = F_2 = 1$, $F_n = F_{n - 1} + F_{n - 2}$ for all $n \geq 3$. 
# Let $s_n = F_{2n - 1} \mod N$ and let $t_n = F_{2n} \mod N$. Start with an 
# array of integers $A = (A[0], \cdots, A[N - 1])$ where initially every 
# $A\text{[}i]$ is equal to $i$. Now perform $K$ successive operations on $A$, 
# where the $j$-th operation consists of reversing the order of those elements 
# in $A$ with indices between $s_j$ and $t_j$ (both ends inclusive). Define 
# $R(N,K)$ to be $\sum_{i = 0}^{N - 1}i \times A\text {[}i]$ after $K$ 
# operations. For example, $R(5, 4) = 27$, as can be seen from the following 
# procedure:Initial position: $(0, 1, 2, 3, 4)$Step 1 - Reverse $A[1]$ to 
# $A[1]$: $(0, 1, 2, 3, 4)$Step 2 - Reverse $A[2]$ to $A[3]$: $(0, 1, 3, 2, 
# 4)$Step 3 - Reverse $A[0]$ to $A[3]$: $(2, 3, 1, 0, 4)$Step 4 - Reverse 
# $A[3]$ to $A[1]$: $(2, 0, 1, 3, 4)$$R(5, 4) = 0 \times 2 + 1 \times 0 + 2 
# \times 1 + 3 \times 3 + 4 \times 4 = 27$Also, $R(10^2, 10^2) = 246597$ and 
# $R(10^4, 10^4) = 249275481640$. Find $R(10^{18}, 10^6)$ giving your answer 
# modulo $10^9$.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
