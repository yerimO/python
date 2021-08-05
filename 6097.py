a,b=list(map(int,input().split()))
li=[[0 for i in range(b)] for j in range(a)]
c=int(input())
l=[]
for k in range(0,c,1):
   l=list(map(int,input().split()))
   for y in range(0,l[0],1):
       if l[1]==1:
           li[(l[2]-1)+y][l[3]-1]=1
       elif l[1]==0:
           li[l[2]-1][(l[3]-1)+y]=1

for i in range(a):
    for j in range(b):
        print(li[i][j],end=' ')
    print('')