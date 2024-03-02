# Problem: Stack Stabilization

# There is a stack of N inflatable discs, with the ith disc from the top having an initial radius of Ri inches.
# The stack is considered unstable if it includes at least one disc whose radius is larger than or equal to that of the disc directly under it. In other words, for the stack to be stable, each disc must have a strictly smaller radius than that of the disc directly under it.
# As long as the stack is unstable, you can repeatedly choose a disc and perform one of the following operations:

# Inflate the disc, increasing its radius by 1 inch. This operation takes A seconds and may be performed on discs of any radius (even those that exceed 10**9 inches).
# Deflate the disc, decreasing its radius by 1 inch. This operation takes B seconds and may only be performed if the resulting radius is a positive integer number of inches (that is, if the disc has a radius of at least 2" before being deflated).
# Determine the minimum number of seconds needed in order to make the stack stable.

# Constraints:
# 1 <= N <= 50
# 1 <= Ri <= 1,000,000,000
# 1 <= A, B <= 100

from typing import List
# Write any import statements here

def getMinimumSecondsRequired(N: int, R: List[int], A: int, B: int) -> int:
  st = [(0,0,0)]
  for val in R:
    tmp = []
    for i in range(len(st)):
      thresh, sl, cst = st[i]
      thresh+=1
      if thresh<val:
        sl-=B
        cst+=(val-thresh)*B
        if not tmp or tmp[-1][-1]>cst:
          tmp.append((thresh, min(sl, 0), cst))
      else:
        if tmp and tmp[-1][0]<val<thresh:
          lst_t, lst_s, lst_cst = st[i-1]
          new_cst = lst_cst+lst_s*(val-1-lst_t)
          if not tmp or tmp[-1][-1]>new_cst:
            tmp.append((val, min(0, lst_s+A), new_cst))
        cst+=(thresh-val)*A
        sl+=A
        if not tmp or tmp[-1][-1]>cst:
          tmp.append((thresh, min(0, sl), cst))
    if tmp[-1][0]<val:
        lst_t, lst_s, lst_cst = st[-1]
        new_cst = lst_cst+lst_s*(val-1-lst_t)
        if not tmp or tmp[-1][-1]>new_cst:
          tmp.append((val, min(0, lst_s+A), new_cst))
    st = tmp
  return st[-1][-1]
