## Problem: All Wrong
## There's a multiple-choice test with N questions, numbered from 1 to N. Each
## question has 2 answer options, labelled A and B. You know that the correct
## answer for the ith question is the ith character in the string C, which is
## either "A" or "B", but you want to get a score of 0 on this test by answering
## every question incorrectly.

## Your task is to implement the function getWrongAnswers(N, C) which returns a
## string with N characters, the ith of which is the answer you should give for
## question i in order to get it wrong (either "A" or "B").

## Constraints:
## 1 <= N <= 100
## C{i} ∈ {'A', 'B'}

## Solution
## Time Complexity: O(N)
## Space Complexity: O(N)
## Explanation: None

from typing import List

def getWrongAnswers(N: int, C: str) -> str:
    mp = {}
    mp['A'], mp['B'] = 'B','A'
    ans = ''
    for a in C:
    ans+=mp[a]
    return ans
