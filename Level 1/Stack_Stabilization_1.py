## Problem: Stack Stabilization 1
## There's a stack of N inflatable discs, with the ith disc from the top having
## an initial radius of R{i} inches.

## The stack is considered unstable if it includes at least one disc whose
## radius is larger than or equal to that of the disc directly under it. In
## other words, for the stack to be stable, each disc must have a strictly
## smaller radius than that of the disc directly under it.

## As long as the stack is unstable, you can repeatedly choose any disc of your
## choice and deflate it down to have a radius of your choice which is strictly
## smaller than the disc’s prior radius. The new radius must be a positive
## integer number of inches.

## Determine the minimum number of discs which need to be deflated in order to
## make the stack stable, if this is possible at all. If it is impossible to
## stabilize the stack, return -1 instead.

## Constraints:
## 1 <= N <= 50
## 1 <= R{i} <= 1,000,000,000


from typing import List
# Write any import statements here

def getMinimumDeflatedDiscCount(N: int, R: List[int]) -> int:
  ans, lst = 0, R[-1]
  for i in range(N-2,-1,-1):
    if R[i]>=lst:
      R[i] = lst-1
      ans+=1
      if lst-1 == 0:
        return -1
    lst = R[i]
  return ans