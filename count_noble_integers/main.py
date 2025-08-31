import sys
from typing import List, Dict



sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

t = int(input())

def count_noble_integers(arr:List[int]):
    arr.sort()
    count,idx=0,0
    while idx<len(arr):
        if arr[idx]!=idx or (idx-1>=0 and arr[idx]==arr[idx-1]):
            idx+=1
            continue
        val = arr[idx]
        while idx<len(arr) and arr[idx]==val:
            count+=1
            idx+=1
    return count
    

while t > 0:
    arr = list(map(int,input().split()))
    print(count_noble_integers(arr))
    t -= 1
