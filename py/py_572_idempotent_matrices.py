# Solution of;
# Project Euler Problem 572: Idempotent matrices
# https://projecteuler.net/problem=572
# 
# A matrix $M$ is called idempotent if $M^2 = M$. Let $M$ be a three by three 
# matrix : $M=\begin{pmatrix} a & b & c\\ d & e & f\\ g &h &i\\\end{pmatrix}$. 
# Let C(n) be the number of idempotent three by three matrices $M$ with 
# integer elements such that$ -n \le a,b,c,d,e,f,g,h,i \le n$. C(1)=164 and 
# C(2)=848. Find C(200).
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
