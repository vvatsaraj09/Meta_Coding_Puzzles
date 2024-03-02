## Problem: Rabbit Hole 2
## You're having a grand old time clicking through the rabbit hole that is your
## favorite online encyclopedia.

## The encyclopedia consists of N different web pages, numbered from 1 to N.
## There are M links present across the pages, the ith of which is present on
## page A{i} and links to a different page B{i}. A page may include multiple
## links, including multiple leading to the same other page.

## A session spent on this website involves beginning on one of the N pages,
## and then navigating around using the links until you decide to stop. That is,
## while on page i, you may either move to any of the pages linked to from it,
## or stop your browsing session.

## Assuming you can choose which page you begin the session on, what's the
## maximum number of different pages you can visit in a single session? Note
## that a page only counts once even if visited multiple times during the
## session.

## Constraints:
## 2 <= N <= 500,000
## 1 <= M <= 500,000
## 1 <= A, B <= N
## A{i} ≠ B{i}

from typing import List
# Write any import statements here
from collections import defaultdict

def getMaxVisitableWebpages(N: int, M: int, A: List[int], B: List[int]) -> int:

  start, page, page_cluster, st, vis = 1, [0 for _ in range(N+1)], [0 for _ in range(N+1)], [], []
  ans = [0 for _ in range(N+1)]
  links, unvisited = defaultdict(set), []
  for a,b in zip(A, B):
    links[a].add(b)
  for i in range(N+1):
    unvisited.append(list(links[i]))
  for i in range(1,N+1):
    if page[i] != 0:
      continue
    st.append(i)
    while len(st)>0:
      val, cycle = st.pop(), False
      if val>0:
        page[val], page_cluster[val] = start, start
        start+=1
        vis.append(val)
        tmp = unvisited[val]
        while tmp:
          new_tmp = tmp[-1]
          if page[new_tmp] == 0:
            st+=[(-1)*val, new_tmp]
            cycle = True
            break
          if page[new_tmp]>0:
            page_cluster[val] = min(page_cluster[val], page_cluster[new_tmp])
          del tmp[-1]
      else:
        val*=(-1)
        tmp = unvisited[val]
        new_tmp = tmp[-1]
        page_cluster[val] = min(page_cluster[val], page_cluster[new_tmp])
        tmp.pop()
        while tmp:
          new_tmp = tmp[-1]
          if page[new_tmp] == 0:
            st+=[(-1)*val, new_tmp]
            cycle = True
            break
          elif page[new_tmp]>0:
            page_cluster[val] = min(page_cluster[val], page_cluster[new_tmp])
          del tmp[-1]
      if cycle:
        continue
      if page[val] == page_cluster[val]:
        previous = vis.pop()
        page[previous] *= -page[val]
        scc, size = [previous], 1

        while previous != val:
            previous = vis.pop()
            page[previous] *= -page[val]
            scc+=[previous]
            size += 1

        st_links = set()
        for pages in scc:
            st_links.update(links[pages])

        st_links.difference_update(scc)

        maxer = size + max([0] + [ans[pages] for pages in st_links])

        for pages in scc:
            ans[pages] = maxer
  return max(ans)