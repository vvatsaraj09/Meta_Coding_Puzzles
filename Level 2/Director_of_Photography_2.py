## Problem: Director of Photography 2
## A photography set consists of N cells in a row, numbered from 1 to N in
## order, and can be represented by a string C of length N. Each cell i is one
## of the following types (indicated by C{i}, the ith character of C):

##      If C{i} = 'P', it is allowed to contain a photographer
##      If C{i} = 'A', it is allowed to contain an actor
##      If C{i} = 'B', it is allowed to contain a backdrop
##      If C{i} = '.', it must be left empty

## A photograph consists of a photographer, an actor, and a backdrop, such that
## each of them is placed in a valid cell, and such that the actor is between
## the photographer and the backdrop. Such a photograph is considered artistic
## if the distance between the photographer and the actor is between X and Y
## cells (inclusive), and the distance between the actor and the backdrop is
## also between X and Y cells (inclusive). The distance between cells i and j
## is |i - j| (the absolute value of the difference between their indices).

## Determine the number of different artistic photographs which could
## potentially be taken at the set. Two photographs are considered different if
## they involve a different photographer cell, actor cell, and/or backdrop cell.

## Constraints:
## 1 <= N <= 300,000
## 1 <= X <= Y <= N

# Write any import statements here

def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
  p,b,ans = [0 for _ in range(N+1)], [0 for _ in range(N+1)],0
  for i in range(N):
    p[i]+=p[i-1]
    b[i]+=b[i-1]
    if C[i] == 'P':
      p[i]+=1
    elif C[i] == 'B':
      b[i]+=1
  for i in range(N):
    if C[i] == 'A':
      ans+=((p[max(i-X, -1)]-p[max(i-Y-1, -1)])*(b[min(i+Y, N-1)]-b[min(i+X-1, N-1)]))
      ans+=((b[max(i-X, -1)]-b[max(i-Y-1, -1)])*(p[min(i+Y, N-1)]-p[min(i+X-1, N-1)]))
  return ans
