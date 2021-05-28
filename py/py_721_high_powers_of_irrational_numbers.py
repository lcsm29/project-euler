# Solution of;
# Project Euler Problem 721: High powers of irrational numbers
# https://projecteuler.net/problem=721
# 
# Given is the function 
# $f(a,n)=\lfloor{(\lceil{\sqrt{a}\:\rceil}+\sqrt{a}\:)^n}\rfloor$. $\lfloor{. 
# }\rfloor$ denotes the floor function and $\lceil{. }\rceil$ denotes the 
# ceiling function. $f(5,2)=27$ and $f(5,5)=3935$. $G(n) = \displaystyle 
# \sum_{a=1}^n f(a, a^2). $$G(1000) \text{ mod } 999\,999\,937=163861845. 
# $Find $G(5\,000\,000). $ Give your answer modulo $999\,999\,937$.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
