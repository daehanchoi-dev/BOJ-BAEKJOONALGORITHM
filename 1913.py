
import copy

n = int(input())
m = int(input())

snail = []
temp = []

for i in range(n):
    temp.append(0)

print('temp',temp)

for i in range(n):
    snail.append(copy.deepcopy(temp))

print('snail',snail)

move = [[0,1],[1,0],[0,-1],[-1,0]]
d = 0
now_x =0; now_y = 0; now_num = n*n


while(now_num > 0):
    snail[now_y][now_x] = now_num
    if(now_x + move[d][0] < 0 or now_x + move[d][0] >= n
            or now_y + move[d][1] < 0 or now_y + move[d][1] >= n
            or snail[now_y+move[d][1]][now_x+move[d][0]] != 0):
        d = (d+1) % 4
    now_y = now_y + move[d][1]
    now_x = now_x + move[d][0]
    now_num = now_num -1

print('snail after while',snail)
print(now_num)
print('snail',snail[0][0])

for i in range(n):
    for j in range(n):
        if(snail[i][j] == m):
            temp_x = i
            temp_y = j
        print(snail[i][j], end= ' ')
    print()
print(temp_x+1, temp_y+1)


"""
1 .(n = 4) ,now_x + move[d][0] = 0 + 0 = 0(해당 안됨),now_y + move[d][1] = 0 + 1 = 1(해당 안됨),snail[0+1][0+0] = 0(해당 안됨)
-> 아무것도 해당 되는 조건이 없으므로, now_y = 0 + 1 = 1, now_x = 0 + 0 = 0, now_num = 16 - 1 = 15
2 .(n = 4) ,now_x + move[d][0] = 0 + 0 = 0(해당 안됨),now_y + move[d][1] = 1 + 1 = 2(해당 안됨),snail[1+1][0+0] = 0(해당 안됨)
-> 아무것도 해당 되는 조건이 없으므로, now_y = 1 + 1 = 2, now_x = 0 + 0 = 0, now_num = 15 - 1 = 14
3 .(n = 4) ,now_x + move[d][0] = 0 + 0 = 0(해당 안됨),now_y + move[d][1] = 2 + 1 = 3(해당 안됨),snail[2+1][0+0] = 0(해당 안됨)
-> 아무것도 해당 되는 조건이 없으므로, now_y = 2 + 1 = 3, now_x = 0 + 0 = 0, now_num = 14 - 1 = 13
4 .(n = 4) ,now_x + move[d][0] = 0 + 0 = 0(해당 안됨),now_y + move[d][1] = 3 + 1 = 4(해당 됨), snail[3+1][0+0] = 0(해당 안됨)
-> now_y+move[d][1] >= n 의 조건을 만족시키므로 => d = (0+1) % 4 = 1
-> now_y = 3 + 0 = 3, now_x = 0 + 1, now_num = 13 - 1 = 12
5 .(n = 4) ,now_x + move[d][0] = 1 + 1 = 2(해당 안됨),now_y + move[d][1] = 3 + 0 = 3(해당 안됨),snail[3+0][1+1] = 0(해당 안됨)
-> 아무것도 해당 되는 조건이 없으므로, now_y = 3 + 0 = 3, now_x = 1+1 = 2, now_num = 13-1 = 12
6 .(n = 4), now_x + move[d][0] = 2 + 1 = 3(해당 안됨),now_y + move[d][1] = 3 + 0 = 3(해당 안됨),snail[3+0][2+1] = 0(해당 안됨)
-> 아무것도 해당 되는 조건이 없으므로, now_y = 3 + 0 = 3, now_x = 2+1 = 3, now_num = 12-1 = 11
7 .(n = 4), now_x + move[d][0] = 3 + 1 = 4(해당 됨),now_y + move[d][1] = 3 + 0 = 3(해당 안됨),snail[3+0][3+1] = 0(해당 안됨)
-> now_x + move[d][0] >= 4 의 조건을 만족시키므로 => d = (1+1) % 4 = 2
-> now_y = 3 - 1 = 2, now_x = 3 + 0 = 3, now_num = 11 - 1 = 10
8 .(n = 4), now_x + move[d][0] = 3 + 0 = 3(해당 안됨),now_y + move[d][1] = 2 - 1 = 1(해당 안됨),snail[2-1][4+0] = 0(해당 안됨)
-> now_x + move[d][0] >= 4 의 조건을 만족시키므로 => d = (2+1) % 4 = 3
-> now_y = 2 + 0 = 2, now_x - 1 = 4 - 1 = 3, now_num = 10 - 1 = 9
9 .(n = 4), now_x + move[d][0] = 3 - 1 = 2(해당 안됨),now_y + move[d][1] = 2 + 0 = 2(해당 안됨),snail[2+0][3-1] = 0(해당 안됨)
-> 아무것도 해당 되는 조건이 없으므로, now_y = 2 + 0 = 2, now_x - 1 = 3 - 1 = 2, now_num = 9 - 1 = 8
10.(n = 4), now_x + move[d][0] = 2 - 1 = 1(해당 안됨),now_y + move[d][1] = 2 + 0 = 2(해당 안됨),snail[2+0][2-1] = 0(해당 안됨)
-> 아무것도 해당 되는 조건이 없으므로, now_y = 2 + 0 = 2, now_x - 1 = 2 - 1 = 1, now_num = 8 - 1 = 7
11.(n = 4), now_x + move[d][0] = 1 - 1 = 0(해당 안됨),now_y + move[d][1] = 2 + 0 = 2(해당 안됨),snail[2+0][1-1] = 0(해당 안됨)
-> 아무것도 해당 되는 조건이 없으므로, now_y = 2 + 0 = 2, now_x - 1 = 1 - 1 = 0, now_num = 7 - 1 = 6
11.(n = 4), now_x + move[d][0] = 0 - 1 = -1(해당 됨),now_y + move[d][1] = 2 + 0 = 2(해당 안됨),snail[2+0][-1] = 0(해당 안됨)
-> now_x + move[d][0] < 0 의 조건을 만족시키므로 => d = (3+1) % 4 = 0
-> now_y = 2 + 1 = 3, now_x = 0 + 0 = 0, now_num = 6 - 1 = 5
12.(n = 4), now_x + move[d][0] = 0 + 0 = 0(해당 안됨),now_y + move[d][1] = 3 + 1 = 4(해당 됨),snail[3+1][0+0] = 0(해당 안됨)
-> now_y + move[d][1] >= n 의 조건을 만족시키므로 => d = (0+1) % 4 = 1
-> now_y = 3 + 0 = 3, now_x = 0 + 1 = 1, now_num = 5 - 1 = 4
13.(n = 4), now_x + move[d][0] = 1 + 1 = 2(해당 안됨),now_y + move[d][1] = 3 + 0 = 3(해당 안됨),snail[3+0][1+1] = 0(해당 안됨)
-> 아무것도 해당 되는 조건이 없으므로, now_y = 3 + 0 = 3, now_x + 1 = 1 + 1 = 2, now_num = 4 - 1 = 3
14.(n = 4), now_x + move[d][0] = 2 + 1 = 3(해당 안됨),now_y + move[d][1] = 3 + 0 = 3(해당 안됨),snail[3+0][2+1] = 0(해당 안됨)
-> 아무것도 해당 되는 조건이 없으므로, now_y = 3 + 0 = 3, now_x + 1 = 2 + 1 = 3, now_num = 3 - 1 = 2
15.(n = 4), now_x + move[d][0] = 3 + 1 = 4(해당 됨),now_y + move[d][1] = 3 + 0 = 3(해당 안됨),snail[3+0][3+1] = 0(해당 안됨)
-> now_x + move[d][0] >= n 의 조건을 만족시키므로 => d = (1+1) % 4 = 2,
-> now_y = 3 - 1 = 2, now_x = 3 + 0 = 3, now_num = 2 - 1 = 0
"""

"""
49 26 27 28 29 30 31
48 25 10 11 12 13 32
47 24  9  2  3 14 33
46 23  8  1  4 15 34
45 22  7  6  5 16 35
44 21 20 19 18 17 36
43 42 41 40 39 38 37

36 17 18 19 20 21
35 16  5  6  7 22
34 15  4  1  8 23
33 14  3  2  9 24
32 13 12 11 10 25
31 30 29 28 27 26

16  5  6  7
15  4  1  8
14  3  2  9
13 12 11 10
  
"""


