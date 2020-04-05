# Dynamic Programming
X = int(input())
cnt = 0
minimum = [X]

def cal(X):
    lst = []
    for i in X:
        lst.append(i-1)
        if i%3 ==0:
            lst.append(i/3)
        if i%2 ==0:
            lst.append(i/2)
    lst = set(lst)
    lst = list(lst)
    return lst

while True:
    if X==1:
        print("Count :",cnt)
        break
    Dp = minimum
    minimum = []
    minimum = cal(Dp)
    cnt += 1
    if min(minimum) == 1:
        print("Count ", cnt)
        break
