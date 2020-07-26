N, C = map(int, input().split())
M = int(input())
Box = [list(map(int, input().split())) for _ in range(M)]

from_ =0
to_ = 0
val_ = 0
Sum = 0
Total = 0
cnt = 0
cnt_ = 0

Box.sort(reverse=False)
print(Box)


for i in range(M):
    from_ = Box[i][0]
    to_ = Box[i][1]
    val_ = Box[i][2]
    if from_ == 1:
        Sum += val_
        cnt += 1
        if Sum >= C:
            Sum = C
            Total = Sum
            for j in range(cnt):
                if Box[j][1] == 2:
                    Sum -= Box[j][2]
                    Total += Box[j][2]

    if from_ == 2:
        Sum += val_
        cnt_ += 1
        if Sum >= C:
            Sum = C
            for k in range(cnt_):
                if Box[k][1] == 3:
                    Sum -= Box[k][2]
                    Total += Box[k][2]


print(Total)












    
