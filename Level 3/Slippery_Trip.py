## Problem: Slippery Trip
## There's a grid of cells with R rows (numbered from 1 to R from top to bottom)
## and C columns (numbered from 1 to C from left to right). The grid wraps
## around horizontally, meaning that column 1 is just to the right of column C
## (and column C is just to the left of column 1).

## The cell in row i and column j initially contains one of the following
## (indicated by the character G{i,j}):

##      If G{i,j} = '.', the cell is empty.
##      If G{i,j} = '*', the cell contains a coin.
##      If G{i,j} = '>', the cell contains an arrow pointing right.
##      If G{i,j} = 'v', the cell contains an arrow pointing down.

## You may cyclically shift each row to the right as many times as you'd like
## (including not at all). Each such shift causes each of the row's cells to
## move 1 column to the right, with its rightmost cell (in column C) wrapping
## around and moving to column 1.

## After you've finished rotating the rows to your liking, you'll take a trip
## through the grid, starting by entering the cell at the top-left corner (in
## row 11 and column 11) downward from above the grid. Upon entering a cell, if
## it contains a coin that you haven't yet collected, you'll collect it. If it
## contains an arrow, your direction of travel will change to that of the arrow
## (either right or down). Either way, you'll then proceed to the next adjacent
## cell in your direction of travel. If you move rightward from column C, you'll
## wrap around to column 1 in the same row, and if you move downward from row R,
## you'll end your trip. Note that you may only collect each cell's coin at most
## once, that your trip might last forever, and that once you begin your trip
## you cannot shift the grid's rows further.

## Determine the maximum number of coins you can collect on your trip.

## Constraints:
## 2 <= R, C <= 400,000
## R * C <= 800,000
## G{i, j} ∈ {'.', '*', '>', 'v'}

from typing import List
# Write any import statements here

def getMaxCollectableCoins(R: int, C: int, G: List[List[str]]) -> int:
  def function(row, C):
    coins, right, down, cumulativeS, row_terminates, pro_terminates, ans, fl_right = 0, -1, -1, [0], False, False, 0, False 
    for i in range(C):
      if row[i] == '*':
        coins+=1
      elif row[i] == '>':
        fl_right = True
        right = (right if right!=-1 else i)
      elif row[i] == 'v':
        down = (down if down!=-1 else i)
        if right != -1:
          ans = max(ans, cumulativeS[i]-cumulativeS[right])
        right = -1
      cumulativeS.append(coins)
    if fl_right:
      if down == -1:
        row_terminates = True
        ans = coins
        if not coins and right == 0:
          pro_terminates = True
          if any([a!='>' for a in row]):
            pro_terminates = False
      elif right!=-1:
        ans = max(ans, coins-cumulativeS[right]+cumulativeS[down])
    else:
      ans = (1 if coins>0 else 0)
    return ans, row_terminates, pro_terminates
      
  info = []
  for g in G:
    coins, row_terminates, pro_terminates = function(g, C)
    info.append((coins, row_terminates))
    if pro_terminates:
      break
  ans_coins = [0]*len(info)
  for i in range(len(info)-1,-1,-1):
    coins, row_terminates = info[i]
    if row_terminates:
      tmp = (1 if coins else 0)
      ans_coins.append(max(ans_coins[-1]+tmp, coins))
    else:
      ans_coins.append(ans_coins[-1]+coins)
  return ans_coins[-1]
