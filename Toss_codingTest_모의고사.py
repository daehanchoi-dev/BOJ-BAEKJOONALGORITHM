"""
n(1,000 이하의 자연수)을 입력하고 n 이하의 자연수 중
3의 배수, 5의 배수의 합을 구하는 프로그램을 작성하십시오.
"""

user_input = int(input())
sum = 0

for i in range(3, user_input + 1):
    if i % 3 == 0:
        sum += i
    if i % 5 == 0:
        sum += i
    if i % 15 == 0:
        sum -= i

print(sum)

"""
2017/2018 시즌 영국 축구 1부 리그의 득점과 도움 기록을 가진 테이블이 있습니다.

도움이 5개 이상인 선수 중에서 득점 기록에 대하여 내림차순으로 정렬하여 출력 형식에 맞게 출력하십시오.

테이블 구조는 아래와 같습니다.

PLAYERSTAT

NAME(이름)	GOALS(득점)	ASSISTS(도움)
VARCHAR(20)	INT	        INT

출력 설명
NAME GOALS ASSISTS
"""
"""

select name, goals, assists
from PLAYERSTAT
where assists >= 5
order by goals desc;

"""