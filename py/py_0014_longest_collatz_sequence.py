# Solution of;
# Project Euler Problem 14: Longest Collatz sequence
# https://projecteuler.net/problem=14
# 
# The following iterative sequence is defined for the set of positive ints:
# 
#   n → n/2 (n is even)
#   n → 3n + 1 (n is odd)
# 
# Using the rule above and starting with 13, we generate the following seq:
# 
#   13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# 
# It can be seen that this sequence (starting at 13 and # finishing at 1) 
# contains 10 terms. Although it has not been proved yet (Collatz Problem), 
# it is thought that all starting numbers finish at 1. 
#
# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed

''' removed because it took nearly 10 seconds
def fn_brute(n):
    longest_chain_len = 0
    for i in range(1, n):
        tmp = i
        counter = 0
        while tmp > 1:
            if tmp % 2 == 0:
                tmp //= 2
            else:
                tmp = 3 * tmp + 1
            counter += 1
        if counter > longest_chain_len:
            longest_chain_len = counter
            starting_num = i
    return starting_num
'''

def fn_recursive(n):
    def recursive(num, cache = {}):
        if num == 1:
            return 1
        if num in cache.keys():
            return cache[num]
        else:
            if num % 2 == 0:
                new_num = num // 2
            else:
                new_num = 3 * num + 1
            cache[num] = recursive(new_num) + 1
            return cache[num]
    
    starting_num = max(range(1, n), key=recursive)
    return starting_num


if __name__ == '__main__':
    n = 1_000_000
    i = 1
    prob_id = 14
    # timed.caller(fn_brute, n, i, prob_id)
    timed.caller(fn_recursive, n, i, prob_id)
