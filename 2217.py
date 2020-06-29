def solution(rope):
    ans = 0
    rope.sort(reverse=True)
    for i in range(N):
        rope[i] = rope[i] * (i+1)

    return max(rope)


N = int(input())
rope = []
for _ in range(N):
    rope.append(int(input()))

print(solution(rope))
