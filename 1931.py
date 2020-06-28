import sys

N = int(sys.stdin.readline())
meeting = sorted([list(map(int, sys.stdin.readline().split())) for i in range(N)],
                 key=lambda x: (x[1], x[0]))

end = answer = 0

for i in range(meeting):
    if end <= i[0]:
        end = i[1]
        answer += 1

print(answer)