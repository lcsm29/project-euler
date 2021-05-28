# Solution of;
# Project Euler Problem 580: Squarefree Hilbert numbers
# https://projecteuler.net/problem=580
# 
# A Hilbert number is any positive integer of the form $4k+1$ for integer 
# $k\geq 0$. We shall define a squarefree Hilbert number as a Hilbert number 
# which is not divisible by the square of any Hilbert number other than one. 
# For example, $117$ is a squarefree Hilbert number, equaling $9\times13$. 
# However $6237$ is a Hilbert number that is not squarefree in this sense, as 
# it is divisible by $9^2$. The number $3969$ is also not squarefree, as it is 
# divisible by both $9^2$ and $21^2$. There are $2327192$ squarefree Hilbert 
# numbers below $10^7$. How many squarefree Hilbert numbers are there below 
# $10^{16}$?
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
