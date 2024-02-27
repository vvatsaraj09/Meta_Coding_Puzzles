 Problem: Rotary Lock 1
## You're trying to open a lock. The lock comes with a wheel which has the
## integers from 1 to N arranged in a circle in order around it (with integers
## 1 and N adjacent to one another). The wheel is initially pointing at 1.

## It takes 1 second to rotate the wheel by 1 unit to an adjacent integer in
## either direction, and it takes no time to select an integer once the wheel
## is pointing at it.

## The lock will open if you enter a certain code. The code consists of a
## sequence of M integers, the ith of which is C{i}. Determine the minimum
## number of seconds required to select all M of the code's integers in order.

## Constraints:
## 3 <= N <= 50,000,000
## 1 <= M <= 1,000
## 1 <= C{i} <= N

from typing import List
# Write any import statements here

def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
  curr, ans = 1, 0
  for a in C:
    ans+=min(abs(curr-a), N-max(curr, a)+min(a,curr))
    curr = a
  return ans
