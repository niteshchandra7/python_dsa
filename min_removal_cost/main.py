import sys
from typing import List, Dict

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

t = int(input())

def solve(arr:List[int])->int:
    arr.sort(reverse=True)
    arr_sum = 0
    for elem in arr:
        arr_sum+=elem
    ans=0;
    for elem in arr:
        ans+=arr_sum
        arr_sum-=elem
    return ans
    
    

while t > 0:
    arr = list(map(int,input().split()))
    print(solve(arr))
    t -= 1
