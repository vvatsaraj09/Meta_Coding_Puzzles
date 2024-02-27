## Problem: Scoreboard Inference 1
## You are spectating a programming contest with N competitors, each trying to
## independently solve the same set of programming problems. Each problem has a
## point value, which is either 1 or 2.

## On the scoreboard, you observe that the ith competitor has attained a score
## of S{i}, which is a positive integer equal to the sum of the point values of
## all the problems they have solved.

## The scoreboard does not display the number of problems in the contest, nor
## their point values. Using the information available, you would like to
## determine the minimum possible number of problems in the contest.

## Constraints:
## 1 <= N <= 500,000
## 1 <= S{i} <= 1,000,000,000


from typing import List
# Write any import statements here

def getMinProblemCount(N: int, S: List[int]) -> int:
  twos, ones = 0,0
  for a in S:
    ones = max(ones, a%2)
    twos = max(twos, a//2)
  return ones+twos
