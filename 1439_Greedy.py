N = input()
total = 0

for i in range(1, len(N)):
    if N[i] != N[i-1]:
        total += 1

print((total+1)//2)