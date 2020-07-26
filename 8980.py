N, C = map(int, input().split())
M = int(input())

first = 0
second = 0
Sum = 0


for i in range(M):
    Box = list(map(int, input().split()))
    print(Box[0])
    first = Box[0]
    second = Box[1]
    if first == 1:
        Sum += Box[2]
    if Sum >= C:
        Sum = C
    print('Sum= ', Sum)
    
