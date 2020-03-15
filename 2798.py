################## demo ######################
"""
from random import *
M = randint(10, 300)
Sum = 0
cnt = 0
Final_summit = 0

for i in range(21):
    N = randint(1,100)
    Sum += N
    cnt += 1
    print("M=",M, "cnt=",cnt, "N=", N, "Sum=",Sum)
    if cnt == 3 and Sum <= M:
        print("최종 합은:", Sum)
        if Final_summit < Sum:
            Final_summit = Sum
            cnt =0
            Sum =0
            print('Final_Summit',Final_summit)
        else:
            cnt = 0
            Sum = 0
    elif cnt == 3 and Sum > M:
        print("다시뽑으시오")
        cnt = 0
        Sum = 0

print("최종 값 :", Final_summit)
"""
################### Summit ######################

M, N = map(int, input().split())
card = list(map(int, input().split('')))
Final_summit = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if(card[i]+card[j]+card[k]) <= M and M - (card[i]+card[j]+card[k]) < M - Final_summit:
                Final_summit = card[i]+card[j]+card[k]

print(Final_summit)



