example = input().split('-')
result = 0
for i in example[0].split('+'):
    result += int(i)

for i in example[1:]:
    for j in i.split('+'):
        result -= int(j)