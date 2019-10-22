# modify this function, and create other functions below as you wish
def question02(risk, bonus, trader):
    # modify and then return the variable below
    lis=[]
    n=len(bonus)
    for i in range(n):
        lis.append([risk[i],bonus[i]])
    lis.sort()
    trader.sort()
    r=-1
    answer = 0
    mx=0
    for l in range(n):
        while(r+1<n and lis[r+1][0]<=trader[l]):
            r+=1
            mx=max(mx,lis[r][1])
        answer+=mx
    return answer

