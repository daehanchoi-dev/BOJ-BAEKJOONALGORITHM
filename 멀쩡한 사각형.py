# 최대공약수를 구하기 위한 함수
def check(a, b):
    GCM = 1
    # a와 b의 공약수 중 최대값(최대 공약수)를 구한다.
    for i in range(1,a+1):
        if a % i == 0 and b % i == 0:
            GCM = max(GCM, i)
    return GCM

# 메인 함수
def solution(w,h):
    ans = 0
    # 최대공약수(g)를 Check 함수를 통해 구한다
    g = check(w,h)
    ans = w*h - (w+h- g)

    return ans




