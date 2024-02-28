## Problem: Rotary Lock 2
## You're trying to open a lock. The lock comes with two wheels, each of which
## has the integers from 1 to N arranged in a circle in order around it (with
## integers 1 and N adjacent to one another). Each wheel is initially pointing
## at 1.

## It takes 1 second to rotate the wheel by 1 unit to an adjacent integer in
## either direction, and it takes no time to select an integer once the wheel is
## pointing at it.

## The lock will open if you enter a certain code. The code consists of a
## sequence of M integers, the ith of which is C{i}. For each integer in the
## sequence, you may select it with either of the two wheels. Determine the
## minimum number of seconds required to select all M of the code's integers
## in order.

## Constraints:
## 3 <= N <= 1,000,000,000
## 1 <= M <= 3,000
## 1 <= C{i} <= N

from typing import List
# Write any import statements here

def getVal(a, curr, N):
  return min(abs(curr-a), N-max(curr, a)+min(a,curr))

def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
  C.insert(0,1)
  M+=1
  ans = [[float('inf') for _ in range(i)] for i in range(M)]
  ans[1][0] = getVal(C[0], C[1], N)
  for i in range(2,M):
      for j in range(i-1):
          ans[i][j] = getVal(C[i-1], C[i], N)+ans[i-1][j]
      for j in range(i-1):
          ans[i][i-1] = min(ans[i][i-1], ans[i-1][j]+getVal(C[j], C[i], N))
  return min(ans[-1])

