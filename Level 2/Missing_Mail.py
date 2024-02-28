## Problem: Missing Mail
## You are the manager of a mail room which is frequently subject to theft. A
## period of N days is about to occur, such that on the ith day, the following
## sequence of events will occur in order:

##  1. A package with a value of V{i} dollars will get delivered to the mail
##     room (unless V{i} = 0, in which case no package will get delivered).
##
##  2. You can choose to pay C dollars to enter the mail room and collect all of
##     the packages there (removing them from the room), and then leave the
##     room.
##
##  3. With probability S, all packages currently in the mail room will get
##     stolen (and therefore removed from the room).

## Note that you're aware of the delivery schedule V{1..N}, but can only observe
## the state of the mail room when you choose to enter it, meaning that you
## won't immediately be aware of whether or not packages were stolen at the end
## of any given day.

## Your profit after the Nth day will be equal to the total value of all
## packages which you collected up to that point, minus the total amount of
## money you spent on entering the mail room.

## Please determine the maximum expected profit you can achieve (in dollars).

## Note: Your return value must have an absolute or relative error of at most
## 10^(-6) to be considered correct.

## Constraints:
## 1 <= N <= 4000
## 0 <= V{i} <= 1000
## 1 <= C <= 1000
## 0.0 <= S <= 1.0


from typing import List
# Write any import statements here

def getMaxExpectedProfit(N: int, V: List[int], C: int, S: float) -> float:
  bfs = [[0,0]]
  for pac in V:
    bfs = [[a*(1-S), b] for a,b in bfs]+[[0,0]]
    bfs[-1][-1] = max([a+b for a,b in bfs])+pac-C
    for i in range(len(bfs)-1):
      bfs[i][0]+=pac
  return max(b for a,b in bfs)
