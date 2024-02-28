## Problem: Portals
## You've found yourself in a grid of cells with R rows and C columns. The cell
## in the ith row from the top and jth column from the left contains one of the
## following (indicated by the character G{i,j}:

##  -   If G{i,j} = '.', the cell is empty.
##  -   If G{i,j} = 'S', the cell contains your starting position. There is
#       exactly one such cell.
##  -   If G{i,j} = 'E', the cell contains an exit. There is at least one such
##      cell.
##  -   If G{i,j} = '#', the cell contains a wall.
##  -   Otherwise, if G{i,j} is a lowercase letter (between "a" and "z",
##      inclusive), the cell contains a portal marked with that letter.

## Your objective is to reach any exit from your starting position as quickly as
## possible. Each second, you may take either of the following actions:

##  -   Walk to a cell adjacent to your current one (directly above, below, to
##      the left, or to the right), as long as you remain within the grid and
##      that cell does not contain a wall.
##  -   If your current cell contains a portal, teleport to any other cell in
##      the grid containing a portal marked with the same letter as your current
##      cell's portal.

## Determine the minimum number of seconds required to reach any exit, if it's
## possible to do so at all. If it's not possible, return -1 instead.

## Constraints:
## 1 <= R, C <= 50
## G{i,j} ∈ {'.', 'S', 'E', '#', 'a' ... 'z'}


from typing import List
# Write any import statements here
from collections import defaultdict
def allowed(i,j, R, C, st):
  if i<0 or j<0 or i == R or j == C:
    return False
  if str(i)+" "+str(j) in st:
    return False
  return True
def getSecondsRequired(R: int, C: int, G: List[List[str]]) -> int:
  st, mp, si, sj = set(), defaultdict(list), 0,0
  for i in range(R):
    for j in range(C):
      if G[i][j] == 'S':
        si,sj = i,j
      elif G[i][j].isalpha() and G[i][j].islower():
        mp[G[i][j]].append(str(i)+" "+str(j))
  bfs = [(si,sj, 0)]
  st.add(str(si)+" "+str(sj))
  while bfs:
    i,j, curr = bfs.pop(0)
    if G[i][j] == 'E':
      return curr
    if G[i][j] == '#':
      continue
    for a,b in [(1,0),(0,1),(0,-1),(-1,0)]:
      i1,j1 = i+a, j+b
      if allowed(i1,j1, R, C, st):
        bfs.append((i1,j1, curr+1))
        st.add(str(i1)+" "+str(j1))
    if G[i][j].isalpha() and G[i][j].islower():
      for val in mp[G[i][j]]:
        a,b = map(int, val.split(" "))
        if allowed(a,b, R, C, st):
          bfs.append((a,b, curr+1))
          st.add(str(a)+" "+str(b))
  return -1
