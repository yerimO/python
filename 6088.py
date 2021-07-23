a,b,c=list(map(int,input().split()))
cnt=0
sum=a
while True:
    cnt+=1
    if(cnt==c):
        print(sum)
        break
    sum+=b
