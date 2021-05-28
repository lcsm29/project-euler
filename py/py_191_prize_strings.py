# Solution of;
# Project Euler Problem 191: Prize Strings
# https://projecteuler.net/problem=191
# 
# A particular school offers cash rewards to children with good attendance and 
# punctuality. If they are absent for three consecutive days or late on more 
# than one occasion then they forfeit their prize. During an n-day period a 
# trinary string is formed for each child consisting of L's (late), O's (on 
# time), and A's (absent). Although there are eighty-one trinary strings for a 
# 4-day period that can be formed, exactly forty-three strings would lead to a 
# prize:OOOO OOOA OOOL OOAO OOAA OOAL OOLO OOLA OAOO OAOAOAOL OAAO OAAL OALO 
# OALA OLOO OLOA OLAO OLAA AOOOAOOA AOOL AOAO AOAA AOAL AOLO AOLA AAOO AAOA 
# AAOLAALO AALA ALOO ALOA ALAO ALAA LOOO LOOA LOAO LOAALAOO LAOA LAAOHow many 
# "prize" strings exist over a 30-day period?
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
