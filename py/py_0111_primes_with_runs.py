# Solution of;
# Project Euler Problem 111: Primes with runs
# https://projecteuler.net/problem=111
# 
# Considering 4-digit primes containing repeated digits it is clear that they 
# cannot all be the same: 1111 is divisible by 11, 2222 is divisible by 22, 
# and so on. But there are nine 4-digit primes containing three ones:1117, 
# 1151, 1171, 1181, 1511, 1811, 2111, 4111, 8111We shall say that M(n, d) 
# represents the maximum number of repeated digits for an n-digit prime where 
# d is the repeated digit, N(n, d) represents the number of such primes, and 
# S(n, d) represents the sum of these primes. So M(4, 1) = 3 is the maximum 
# number of repeated digits for a 4-digit prime where one is the repeated 
# digit, there are N(4, 1) = 9 such primes, and the sum of these primes is 
# S(4, 1) = 22275. It turns out that for d = 0, it is only possible to have 
# M(4, 0) = 2 repeated digits, but there are N(4, 0) = 13 such cases. In the 
# same way we obtain the following results for 4-digit primes. Digit, dM(4, 
# d)N(4, d)S(4, 
# d)02136706113922275231222133124621443288885315557631666173957863831888793748073For 
# d = 0 to 9, the sum of all S(4, d) is 273700. Find the sum of all S(10, d).
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 111
    timed.caller(dummy, n, i, prob_id)
