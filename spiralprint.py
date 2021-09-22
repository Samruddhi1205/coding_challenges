#Print given matrix in spiral form.
'''Input :
1, 2, 3, 4
12, 13, 14, 5
11, 16, 15, 6
10, 9, 8, 7

Output :
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15. 16'''

#python code for spiral printing

def spiralOrder(arr):
    ans=[]
    while arr:
        ans+=arr.pop(0)
        arr= (list(zip(*arr)))[::-1]
    return ans
arr=[]
n,m=map(int,input().split())
for i in range(n):
    arr.append(list(map(int,input().split())))
print(*spiralOrder(arr))
