def solution(n, edge):
    answer = [0]*(n+1)
    newedge=[[] for i in range(len(edge)+1)]
    for i in range(len(edge)):
        if not edge[i][1] in newedge[edge[i][0]]:
            newedge[edge[i][0]].append(edge[i][1])
            newedge[edge[i][0]].sort()
        if not edge[i][0] in newedge[edge[i][1]]:
            newedge[edge[i][1]].append(edge[i][0])
            newedge[edge[i][1]].sort()
    answer[0],answer[1]= -1,-1
    queue=[1]
    count=1
    while not all(answer):
        temp=[]
        for start in queue:
            for i in newedge[start]:
                if answer[i] ==0:
                    answer[i]+=count
                    temp.append(i)
        queue=temp
        count+=1
    ans=answer.count(max(answer))
    return ans