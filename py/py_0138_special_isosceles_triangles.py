# Solution of;
# Project Euler Problem 138: Special isosceles triangles
# https://projecteuler.net/problem=138
# 
# Consider the isosceles triangle with base length, $b = 16$, and legs, $L = 
# 17$. By using the Pythagorean theorem it can be seen that the height of the 
# triangle, $h = \sqrt{17^2 - 8^2} = 15$, which is one less than the base 
# length. With $b = 272$ and $L = 305$, we get $h = 273$, which is one more 
# than the base length, and this is the second smallest isosceles triangle 
# with the property that $h = b \pm 1$. Find $\sum L$ for the twelve smallest 
# isosceles triangles for which $h = b \pm 1$ and $b$, $L$ are positive 
# integers.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 138
    timed.caller(dummy, n, i, prob_id)