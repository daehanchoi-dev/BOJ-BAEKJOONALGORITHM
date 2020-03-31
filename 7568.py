# 덩치 ( Brute Force)
N = int(input())
people = []


for _ in range(N):
    w, h = map(int, input().split())
    people.append((w,h))

for a in people:
    rank =1

    for b in people:
        if(a[0] != b[0]) and (a[1] != b[1]):
            if(a[0] < b[0]) and (a[1] < b[1]):
                rank += 1

    print(rank)


