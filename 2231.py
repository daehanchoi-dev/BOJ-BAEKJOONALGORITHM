#Brute Force
import sys
num = sys.stdin.readline()

gen_num = int(num) - (len(num)*9)

if gen_num < 0:
    gen_num = int(num)

while gen_num < int(num):
    each_num_sum = sum([int(i) for i in str(gen_num)])
    result = each_num_sum + gen_num

    if result == int(num):
        print(gen_num)
        break
    else:
        gen_num +=1

if gen_num == int(num):
    print(0)

