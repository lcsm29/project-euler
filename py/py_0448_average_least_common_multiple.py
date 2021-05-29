# Solution of;
# Project Euler Problem 448: Average least common multiple
# https://projecteuler.net/problem=448
# 
# The function lcm(a,b) denotes the least common multiple of a and b. Let A(n) 
# be the average of the values of lcm(n,i) for 1≤i≤n. E. g: A(2)=(2+2)/2=2 and 
# A(10)=(10+10+30+20+10+30+70+40+90+10)/10=32. Let S(n)=∑ A(k) for 1≤k≤n. 
# S(100)=122726. Find S(99999999019) mod 999999017.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 448
    timed.caller(dummy, n, i, prob_id)
