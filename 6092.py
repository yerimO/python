a=int(input())
li=[]
li=list(map(int,input().split()))

for i in range(1,24,1):
    cnt=0
    for j in li:
        if i==j:
            cnt+=1
    print(cnt,end=' ')