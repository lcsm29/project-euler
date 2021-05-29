# Solution of;
# Project Euler Problem 185: Number Mind
# https://projecteuler.net/problem=185
# 
# The game Number Mind is a variant of the well known game Master Mind. 
# Instead of coloured pegs, you have to guess a secret sequence of digits. 
# After each guess you're only told in how many places you've guessed the 
# correct digit. So, if the sequence was 1234 and you guessed 2036, you'd be 
# told that you have one correct digit; however, you would NOT be told that 
# you also have another digit in the wrong place. For instance, given the 
# following guesses for a 5-digit secret sequence,90342 ;2 correct70794 ;0 
# correct39458 ;2 correct34109 ;1 correct51545 ;2 correct12531 ;1 correctThe 
# correct sequence 39542 is unique. Based on the following 
# guesses,5616185650518293 ;2 correct3847439647293047 ;1 
# correct5855462940810587 ;3 correct9742855507068353 ;3 
# correct4296849643607543 ;3 correct3174248439465858 ;1 
# correct4513559094146117 ;2 correct7890971548908067 ;3 
# correct8157356344118483 ;1 correct2615250744386899 ;2 
# correct8690095851526254 ;3 correct6375711915077050 ;1 
# correct6913859173121360 ;1 correct6442889055042768 ;2 
# correct2321386104303845 ;0 correct2326509471271448 ;2 
# correct5251583379644322 ;2 correct1748270476758276 ;3 
# correct4895722652190306 ;1 correct3041631117224635 ;3 
# correct1841236454324589 ;3 correct2659862637316867 ;2 correctFind the unique 
# 16-digit secret sequence.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 185
    timed.caller(dummy, n, i, prob_id)
