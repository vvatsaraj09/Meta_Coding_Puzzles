## Problem: Rabbit Hole 1
## You're having a grand old time clicking through the rabbit hole that is your
## favorite online encyclopedia.

## The encyclopedia consists of N different web pages, numbered from 1 to N.
## Each page i contains nothing but a single link to a different page L{i}.

## A session spent on this website involves beginning on one of the N pages,
## and then navigating around using the links until you decide to stop. That is,
## while on page i, you may either move to page L{i}, or stop your browsing
## session.

## Assuming you can choose which page you begin the session on, what's the
## maximum number of different pages you can visit in a single session? Note
## that a page only counts once even if visited multiple times during the
## session.

## Constraints:
## 2 <= N <= 500,000
## 1 <= L{i} <= N
## L{i} ≠ i

from typing import List
# Write any import statements here
from collections import defaultdict

def getMaxVisitableWebpages(N: int, L: List[int]) -> int:
  mp = defaultdict(int)
  for i in range(1,N+1):
    if mp[i] != 0:
      continue
    vis, ctr, curr = set(), 0, i
    while mp[curr] == 0:
      vis.add(curr)
      ctr+=1
      mp[curr] = ctr
      curr = L[curr-1]
    if curr in vis:
      cycle = ctr-mp[curr]+1
      mp[curr], t = cycle, L[curr-1]
      while t!=curr:
        mp[t] = cycle
        t = L[t-1]
    else:
      cycle = mp[curr]
      ctr+=cycle
    t = i
    while t!=curr:
      mp[t] = mp[t]*(-1)+ctr+1
      t = L[t-1]
  return max(mp.values())
