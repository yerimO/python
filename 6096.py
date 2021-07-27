#바둑판 ye 생성 및 입력
ye=[]
for i in range(19):
        ye.append(input().split())
        for j in range(19):
            ye[i][j]=int(ye[i][j])

#입력받을 횟수 입력
a=int(input())

for i in range(a):
     a,b=list(map(int,input().split()))
     for i in range(19):
         if ye[a-1][i]==0:
             ye[a-1][i]=1
         else:
             ye[a-1][i]=0

         if ye[i][b-1]==0:
            ye[i][b-1]=1
         else:
             ye[i][b-1]=0

for i in range(19):
     for j in range(19):
         print(ye[i][j],end=' ')
     print()
