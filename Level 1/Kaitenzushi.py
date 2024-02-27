## Problem: Kaitenzushi
## There are N dishes in a row on a kaiten belt, with the ith dish being of type
## D{i}. Some dishes may be of the same type as one another.

## Kaiten Belt: {https://en.wikipedia.org/wiki/Conveyor_belt_sushi}

## You're very hungry, but you'd also like to keep things interesting. The N
## dishes will arrive in front of you, one after another in order, and for each
## one you'll eat it as long as it isn't the same type as any of the previous K
## dishes you've eaten. You eat very fast, so you can consume a dish before the
## next one gets to you. Any dishes you choose not to eat as they pass will be
## eaten by others.

## Determine how many dishes you'll end up eating.

## Constraints:
## 1 <= N <= 500,000
## 1 <= K <= N
## 1 <= D{i} <= 1,000,000


from typing import List
from collections import defaultdict
# Write any import statements here

def getMaximumEatenDishCount(N: int, D: List[int], K: int) -> int:
  mp, ctr = defaultdict(lambda : -float('inf')), 1
  for a in D:
    if ctr-mp[a]>K:
      mp[a] = ctr
      ctr+=1
  return ctr-1