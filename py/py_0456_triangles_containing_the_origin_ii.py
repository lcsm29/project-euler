# Solution of;
# Project Euler Problem 456: Triangles containing the origin II
# https://projecteuler.net/problem=456
# 
# Define:xn = (1248n mod 32323) - 16161yn = (8421n mod 30103) - 15051Pn = 
# {(x1, y1), (x2, y2), . . . , (xn, yn)}For example, P8 = {(-14913, -6630), 
# (-10161, 5625), (5226, 11896), (8340, -10778), (15852, -5203), (-15165, 
# 11295), (-1427, -14495), (12407, 1060)}. Let C(n) be the number of triangles 
# whose vertices are in Pn which contain the origin in the interior. 
# Examples:C(8) = 20C(600) = 8950634C(40 000) = 2666610948988Find C(2 000 
# 000).
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 456
    timed.caller(dummy, n, i, prob_id)
