# Solution of;
# Project Euler Problem 277: A Modified Collatz sequence
# https://projecteuler.net/problem=277
# 
# A modified Collatz sequence of integers is obtained from a starting value 
# $a_1$ in the following way:$a_{n+1} = \, \,\, \frac {a_n} 3 \quad$ if $a_n$ 
# is divisible by $3$. We shall denote this as a large downward step, "D". 
# $a_{n+1} = \frac {4 a_n+2} 3 \, \,$ if $a_n$ divided by $3$ gives a 
# remainder of $1$. We shall denote this as an upward step, "U". $a_{n+1} = 
# \frac {2 a_n -1} 3 \, \,$ if $a_n$ divided by $3$ gives a remainder of $2$. 
# We shall denote this as a small downward step, "d". The sequence terminates 
# when some $a_n = 1$. Given any integer, we can list out the sequence of 
# steps. For instance if $a_1=231$, then the sequence 
# $\{a_n\}=\{231,77,51,17,11,7,10,14,9,3,1\}$ corresponds to the steps 
# "DdDddUUdDD". Of course, there are other sequences that begin with that same 
# sequence "DdDddUUdDD. . . . ". For instance, if $a_1=1004064$, then the 
# sequence is DdDddUUdDDDdUDUUUdDdUUDDDUdDD. In fact, $1004064$ is the 
# smallest possible $a_1 > 10^6$ that begins with the sequence DdDddUUdDD. 
# What is the smallest $a_1 > 10^{15}$ that begins with the sequence 
# "UDDDUdddDDUDDddDdDddDDUDDdUUDd"?
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 277
    timed.caller(dummy, n, i, prob_id)
