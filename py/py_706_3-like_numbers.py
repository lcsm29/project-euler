# Solution of;
# Project Euler Problem 706: 3-Like Numbers
# https://projecteuler.net/problem=706
# 
# For a positive integer $n$, define $f(n)$ to be the number of non-empty 
# substrings of $n$ that are divisible by 3. For example, the string "2573" 
# has 10 non-empty substrings, three of which represent numbers that are 
# divisible by 3, namely 57, 573 and 3. So $f(2573) = 3$. If $f(n)$ is 
# divisible by 3 then we say that $n$ is 3-like. Define $F(d)$ to be how many 
# $d$ digit numbers are 3-like. For example, $F(2) = 30$ and $F(6) = 290898$. 
# Find $F(10^5)$. Give your answer modulo $1\,000\,000\,007$.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
