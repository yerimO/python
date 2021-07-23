a,b,c,d=list(map(int,input().split()))
cnt=0
sum=a
while True : 
    cnt+=1
    if cnt==d:
        print(sum)
        break
    sum=sum*b+c