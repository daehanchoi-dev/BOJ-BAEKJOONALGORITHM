def solution(phone_number):
    phone_number.sort()

    for i in range(len(phone_number)-1):
        if phone_number[i] in phone_number[i+1]:
            return False

    return True

if __name__ == '__main__':
    phone_number = ['119', '97674223', '1195201829']
    phone_number1 = ['123', '456', '789']
    print(solution(phone_number))
    print(solution(phone_number1))





