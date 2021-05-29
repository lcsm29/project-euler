# Solution of;
# Project Euler Problem 228: Minkowski Sums
# https://projecteuler.net/problem=228
# 
# Let Sn be the regular n-sided polygon – or shape – whose vertices vk (k = 
# 1,2,…,n) have coordinates: xk = cos( 2k-1/n ×180° ) yk = sin( 2k-1/n ×180° ) 
# Each Sn is to be interpreted as a filled shape consisting of all points on 
# the perimeter and in the interior. The Minkowski sum, S+T, of two shapes S 
# and T is the result of adding every point in S to every point in T, where 
# point addition is performed coordinate-wise: (u, v) + (x, y) = (u+x, v+y). 
# For example, the sum of S3 and S4 is the six-sided shape shown in pink 
# below:How many sides does S1864 + S1865 + … + S1909 have?
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 228
    timed.caller(dummy, n, i, prob_id)
