# Solution of;
# Project Euler Problem 244: Sliders
# https://projecteuler.net/problem=244
# 
# You probably know the game Fifteen Puzzle. Here, instead of numbered tiles, 
# we have seven red tiles and eight blue tiles. A move is denoted by the 
# uppercase initial of the direction (Left, Right, Up, Down) in which the tile 
# is slid, e. g. starting from configuration (S), by the sequence LULUR we 
# reach the configuration (E):(S), (E)For each path, its checksum is 
# calculated by (pseudocode):checksum = 0checksum = (checksum × 243 + m1) mod 
# 100 000 007checksum = (checksum × 243 + m2) mod 100 000 007 …checksum = 
# (checksum × 243 + mn) mod 100 000 007where mk is the ASCII value of the kth 
# letter in the move sequence and the ASCII values for the moves 
# are:L76R82U85D68For the sequence LULUR given above, the checksum would be 
# 19761398. Now, starting from configuration (S),find all shortest ways to 
# reach configuration (T). (S), (T)What is the sum of all checksums for the 
# paths having the minimal length?
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
    pass


if __name__ == '__main__':
    n = 1000
    i = 10000
    prob_id = 244
    timed.caller(dummy, n, i, prob_id)
