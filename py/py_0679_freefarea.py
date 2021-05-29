# Solution of;
# Project Euler Problem 679: Freefarea
# https://projecteuler.net/problem=679
# 
# Let $S$ be the set consisting of the four letters 
# $\{\texttt{`A'},\texttt{`E'},\texttt{`F'},\texttt{`R'}\}$. For $n\ge 0$, let 
# $S^*(n)$ denote the set of words of length $n$ consisting of letters 
# belonging to $S$. We designate the words $\texttt{FREE}, \texttt{FARE}, 
# \texttt{AREA}, \texttt{REEF}$ as keywords. Let $f(n)$ be the number of words 
# in $S^*(n)$ that contains all four keywords exactly once. This first happens 
# for $n=9$, and indeed there is a unique 9 lettered word that contain each of 
# the keywords once: $\texttt{FREEFAREA}$So, $f(9)=1$. You are also given that 
# $f(15)=72863$. Find $f(30)$.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 679
    timed.caller(dummy, n, i, prob_id)
