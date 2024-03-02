## Problem: Boss Fight

# There are N warriors, the ith of which has a health of Hi units and can deal Di units of damage per second. 
# They are confronting a boss who has unlimited health and can deal B units of damage per second. Both the warriors and the boss deal damage continuously. 

# For example, in half a second, the boss deals B/2 units of damage. 
# The warriors feel it would be unfair for many of them to fight the boss at once, so they will select just two representatives to go into battle. One warrior i will be the front line, and a different warrior j will back them up. During the battle, the boss will attack warrior i until that warrior is defeated (that is, until the boss has dealt Hi units of damage to them), and will then attack warrior j until that warrior is also defeated, at which point the battle will end. Along the way, each of the two warriors will do damage to the boss as long as they are undefeated.
# Of course, the warriors will never prevail, but they would like to determine the maximum amount of damage they could deal to the boss for any choice of warriors i and j before the battle ends.

# Note: Your return value must have an absolute or relative error of at most.

# Constraints:
# 2 <= N <= 500,000
# 1 <= Hi <= 1,000,000,000
# 1 <= Di <= 1,000,000,000
# 1 <= B <= 1,000,000,000

from typing import List
# Write any import statements here

def getMaxDamageDealt(N: int, H: List[int], D: List[int], B: int) -> float:
  info = [(a, b) for a,b in zip(H, D)]
  info.sort(key = lambda x:(x[0]*x[1]), reverse = True)
  def dfs(ind, first, passed):
    curr_val, curr_ind = 0,0
    for i in range(len(info)):
      if ind == i:
        continue
      health1, dam1 = info[ind]
      health2, dam2 = info[i]
      if first:
        health1, health2 = health2, health1
        dam1, dam2 = dam2, dam1
      damage = health1*(dam1+dam2)+health2*dam2
      if damage>curr_val:
        curr_val, curr_ind = damage, i
    if passed<curr_val:
      return dfs(curr_ind, not first, curr_val)
    return passed
  return max(dfs(0, True, 0), dfs(0, False, 0))/B