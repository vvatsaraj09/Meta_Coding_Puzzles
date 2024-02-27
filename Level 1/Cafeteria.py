## Problem: Cafeteria
## A cafeteria table consists of a row of N seats, numbered from 1 to N from
## left to right. Social distancing guidelines require that every diner be
## seated such that K seats to their left and K seats to their right (or all the
## remaining seats to that side if there are fewer than K) remain empty.

## There are currently M diners seated at the table, the ith of whom is in seat
## S{i}. No two diners are sitting in the same seat, and the social distancing
## guidelines are satisfied.

## Determine the maximum number of additional diners who can potentially sit at
## the table without social distancing guidelines being violated for any new or
## existing diners, assuming that the existing diners cannot move and that the
## additional diners will cooperate to maximize how many of them can sit down.

## Constraints:
## 1 <= N <= 10^(15)
## 1 <= K <= N
## 1 <= M <= 500,000
## M <= N
## 1 <= S{i} <= N


from typing import List
# Write any import statements here

def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
  S.sort()
  S.insert(0, -K)
  S.append(N+K+1)
  K+=1
  ans = 0
  for i in range(len(S)-1):
    ans+=(((S[i+1]-S[i])//K)-1)
  return ans