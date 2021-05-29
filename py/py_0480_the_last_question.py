# Solution of;
# Project Euler Problem 480: The Last Question
# https://projecteuler.net/problem=480
# 
# Consider all the words which can be formed by selecting letters, in any 
# order, from the 
# phrase:thereisasyetinsufficientdataforameaningfulanswerSuppose those with 15 
# letters or less are listed in alphabetical order and numbered sequentially 
# starting at 1. The list would include:1 : a2 : aa3 : aaa4 : aaaa5 : aaaaa6 : 
# aaaaaa7 : aaaaaac8 : aaaaaacd9 : aaaaaacde10 : aaaaaacdee11 : aaaaaacdeee12 
# : aaaaaacdeeee13 : aaaaaacdeeeee14 : aaaaaacdeeeeee15 : aaaaaacdeeeeeef16 : 
# aaaaaacdeeeeeeg17 : aaaaaacdeeeeeeh. . . 28 : aaaaaacdeeeeeey29 : 
# aaaaaacdeeeeef30 : aaaaaacdeeeeefe. . . 115246685191495242: 
# euleoywuttttsss115246685191495243: euler115246685191495244: eulera. . . 
# 525069350231428029: ywuuttttssssrrrDefine P(w) as the position of the word 
# w. Define W(p) as the word in position p. We can see that P(w) and W(p) are 
# inverses: P(W(p)) = p and W(P(w)) = w. Examples:W(10) = 
# aaaaaacdeeP(aaaaaacdee) = 10W(115246685191495243) = eulerP(euler) = 
# 115246685191495243Find W(P(legionary) + P(calorimeters) - P(annihilate) + 
# P(orchestrated) - P(fluttering)). Give your answer using lowercase 
# characters (no punctuation or space).
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 480
    timed.caller(dummy, n, i, prob_id)
