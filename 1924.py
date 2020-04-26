def calender(d, m):
    month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    day = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    piv = 0
    for i in month:
        if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
            for j in range(1, 32):
                if i == d and j == m:
                    print(day[piv])
                else:
                    piv = (piv + 1) % len(day)
        elif i == 4 or i == 6 or i == 9 or i == 11:
            for j in range(1, 31):
                if i == d and j == m:
                    print(day[piv])
                else:
                    piv = (piv + 1) % len(day)
        elif i == 2:
            for j in range(1, 29):
                if i == d and j == m:
                    print(day[piv])
                else:
                    piv = (piv + 1) % len(day)
date = input().split(' ')
x = int(date[0])
y = int(date[1])
calender(x, y)