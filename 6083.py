a,b,c=list(map(int,input().split()))
cnt=0
for i in range(0,a,1):
    for j in range(0,b,1):
        for k in range(0,c,1):
            print(i,j,k,sep=' ')
            cnt+=1
print(cnt)