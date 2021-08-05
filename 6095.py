li=[[0 for j in range(19)]for i in range(19)]
a=int(input())
l=[]
for i in range(0,a,1):
    l=list(map(int,input().split()))
    li[l[0]-1][l[1]-1]=1
for i in range(0,19,1):
    for j in range(0,19,1):
        print(li[i][j],end=' ')
    print('')
     