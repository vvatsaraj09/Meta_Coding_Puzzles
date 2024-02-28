## Problem: Scoreboard Inference 2
## You are spectating a programming contest with N competitors, each trying to
## independently solve the same set of programming problems. Each problem has a
## point value, which is either 1, 2 or 3.

## On the scoreboard, you observe that the iith competitor has attained a score
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
  S = list(set(S))
  one, mandatory_one, mandatory_two, maxer, maxer_2 = False, False, False, 0, 0
  for a in S:
    if a == 1:
      one = True
      mandatory_one = True
    elif a%3 == 1:
      mandatory_one = True
    elif a%3 == 2:
      mandatory_two = True
    if a>=maxer:
      maxer, maxer_2 = a, maxer
    elif a>maxer_2:
      maxer_2 = a
  ans = (maxer//3)
  if mandatory_one:
    ans+=1
  if mandatory_two:
    ans+=1
  if maxer%3 == 0 and mandatory_one and mandatory_two:
    ans-=1
  if maxer%3 == 1 and maxer_2+1!=maxer and not one and mandatory_one:
    ans-=1
  return ans
  