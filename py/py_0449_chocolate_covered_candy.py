# Solution of;
# Project Euler Problem 449: Chocolate covered candy
# https://projecteuler.net/problem=449
# 
# Phil the confectioner is making a new batch of chocolate covered candy. Each 
# candy centre is shaped like an ellipsoid of revolution defined by the 
# equation:$b^2 x^2 + b^2 y^2 + a^2 z^2 = a^2 b^2$. Phil wants to know how 
# much chocolate is needed to cover one candy centre with a uniform coat of 
# chocolate one millimeter thick. If $a = 1$ mm and $b = 1$ mm, the amount of 
# chocolate required is $\dfrac{28}{3} \pi$ mm3If $a = 2$ mm and $b = 1$ mm, 
# the amount of chocolate required is approximately 60. 35475635 mm3. Find the 
# amount of chocolate in mm3 required if $a = 3$ mm and $b =1$ mm. Give your 
# answer as the number rounded to 8 decimal places behind the decimal point.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 449
    timed.caller(dummy, n, i, prob_id)
