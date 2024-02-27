## Problem: Uniform Integers
## A positive integer is considered uniform if all of its digits are equal. For
## example, 222 is uniform, while 223 is not.

## Given two positive integers A and B, determine the number of uniform integers
## between A and B, inclusive.

## Constraints:
## 1 <= A <= B <= 10^(12)

# Write any import statements here
import bisect

def getUniformIntegerCountInInterval(A: int, B: int) -> int:
  lst = []
  for ctr in range(1,13):
    for i in range(1,10):
      lst.append(int(str(i)*ctr))
  
  return bisect.bisect_right(lst, B) - bisect.bisect_left(lst, A)