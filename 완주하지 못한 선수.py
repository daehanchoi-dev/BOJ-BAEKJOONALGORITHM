def solution(participant, completion):
    ans = ''
    temp = []
    for i in range(len(participant)):
        if participant[i] not in completion:
            ans += participant[i]
            
    return ans

if __name__ == "__main__":
    participant = ['Aatrox', 'kevin', 'james', 'joe', 'Leblanc']
    completion = ['kevin', 'james', 'joe']
    print(solution(participant,completion))