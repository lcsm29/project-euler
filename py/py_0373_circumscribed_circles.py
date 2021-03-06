# Solution of;
# Project Euler Problem 373: Circumscribed Circles
# https://projecteuler.net/problem=373
# 
# Every triangle has a circumscribed circle that goes through the three 
# vertices. Consider all integer sided triangles for which the radius of the 
# circumscribed circle is integral as well. Let S(n) be the sum of the radii 
# of the circumscribed circles of all such triangles for which the radius does 
# not exceed n. S(100)=4950 and S(1200)=1653605. Find S(107).
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 373
    timed.caller(dummy, n, i, prob_id)
