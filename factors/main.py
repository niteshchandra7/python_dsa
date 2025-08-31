import sys
from typing import List, Dict

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

t = int(input())

def num_factors(num:int)->int:
    idx:int=1
    count:int=0
    while idx*idx<=num:
        if num%idx==0:
            if idx==num//idx:
                count+=1
            else:
                count+=2
        idx+=1
    return count

def solve(arr:List[int]):
    arr.sort(key=lambda x: (num_factors(x),x))
    return arr

while t > 0:
    arr = list(map(int,input().split()))
    print(solve(arr))
    t -= 1
