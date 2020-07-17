from sys import *
input = stdin.readline

def check():
   for i in range(m):
       s = i        #i가 시작 사다리 위치, s가 현재 사다리 위치
       for j in range(n):
           if a[j][s]: s+=1                    #사다리 표시되어있으면 오른쪽으로
           elif s-1 >=0 and a[j][s-1]: s-=1    #왼쪽이 표시되어 있으면 왼쪽으로
       if s != i: return 0
   return 1
def solve(cnt, x, y):
   res = INF
   if check():
       return cnt
   if cnt == 3:
       return res       #3개 고른 사다리 확인 했으면 더 볼 필요 없음
   for i in range(x, n):        #완탐
       temp = y if x==i else 0
       for j in range(temp, m-1):
           if a[i][j]:
               j+=1
           else:
               a[i][j]=1        #사다리 표시
               res = min(res, solve(cnt+1, i, j+2))
               a[i][j]=0        #사다리 표시 제거
   return res


INF = 1e9
m,k,n = map(int,input().split())
a=[[0]*m for _ in range(n)]
for i in range(k):
   x, y = map(int,input().split())
   a[x-1][y-1] = 1
ans=solve(0,0,0)
print(ans if ans != INF else -1)    #결과가 INF면 3개 이하 없는거, -1 출력