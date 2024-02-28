## Problem: Hops
## A family of frogs in a pond are traveling towards dry land to hibernate. They
## hope to do so by hopping across a trail of N lily pads, numbered from 1 to N
## in order.

## There are F frogs, numbered from 1 to F. Frog i is currently perched atop
## lily pad P{i}. No two frogs are currently on the same lily pad. Lily pad N is
## right next to the shore, and none of the frogs are initially on lily pad N.

## Each second, one frog may hop along the trail towards lily pad N. When a frog
## hops, it moves to the nearest lily pad after its current lily pad which is
## not currently occupied by another frog (hopping over any other frogs on
## intermediate lily pads along the way). If this causes it to reach lily pad N,
## it will immediately exit onto the shore. Multiple frogs may not
## simultaneously hop during the same second.

## Assuming the frogs work together optimally when deciding which frog should
## hop during each second, determine the minimum number of seconds required for
## all F of them to reach the shore.

## Constraints:
## 2 <= N <= 10^(12)
## 1 <= F <= 500,000
## 1 <= P{i} <= N - 1

from typing import List
# Write any import statements here

def getSecondsRequired(N: int, F: int, P: List[int]) -> int:
  P.sort()
  P.append(N)
  ans = F
  for i in range(1,F+1):
    ans+=(P[i]-P[i-1]-1)
  return ans