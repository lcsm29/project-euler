# Solution of;
# Project Euler Problem 607: Marsh Crossing
# https://projecteuler.net/problem=607
# 
# Frodo and Sam need to travel 100 leagues due East from point A to point B. 
# On normal terrain, they can cover 10 leagues per day, and so the journey 
# would take 10 days. However, their path is crossed by a long marsh which 
# runs exactly South-West to North-East, and walking through the marsh will 
# slow them down. The marsh is 50 leagues wide at all points, and the 
# mid-point of AB is located in the middle of the marsh. A map of the region 
# is shown in the diagram below:The marsh consists of 5 distinct regions, each 
# 10 leagues across, as shown by the shading in the map. The strip closest to 
# point A is relatively light marsh, and can be crossed at a speed of 9 
# leagues per day. However, each strip becomes progressively harder to 
# navigate, the speeds going down to 8, 7, 6 and finally 5 leagues per day for 
# the final region of marsh, before it ends and the terrain becomes easier 
# again, with the speed going back to 10 leagues per day. If Frodo and Sam 
# were to head directly East for point B, they would travel exactly 100 
# leagues, and the journey would take approximately 13. 4738 days. However, 
# this time can be shortened if they deviate from the direct path. Find the 
# shortest possible time required to travel from point A to B, and give your 
# answer in days, rounded to 10 decimal places.
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed


def dummy(n):
   pass


if __name__ == '__main__':
   n = 1000
   i = 10000
   timed.caller(dummy, n, i)
