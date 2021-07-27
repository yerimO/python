# 상자 구조 입력 함수 #
def box(li):
    # 박스 내용 입력
    for i in range(10):
        a=list(map(int,input().split()))
        for j in range(10):
            li[i][j]=a[j]
    return li

def RIGHT(li,x,y):
    if li[x][y+1] == 1 and li[x+1][y] == 0:
        return li,x,y
    # 오른쪽 길이 있을 경우 오른쪽으로 이동한다.
    if li[x][y+1]==0:
        y+=1
        li[x][y]=9
    # 아래 먹이가 있을 경우 실행
    elif li[x][y+1]==2:
        y+=1
        li[x][y]=9
        x=8
        y=8
    # 오른쪽 아래 모두 길이 없으면 8,8 리턴
    elif li[x][y+1]==1 and li[x+1][y]==1:
        x=8
        y=8
    return li,x,y


def DOWN(li,x,y):
    # 오른쪽 길이 있을 경우 DOWN 함수를 실행하지 않고 바로 리턴한다.
    if li[x][y+1]==0:
        return li,x,y
    # 아래 길이 있을 경우 아래로 이동한다.
    elif li[x+1][y]==0:
        x+=1
        li[x][y]=9
    # 아래 먹이가 있을 경우 실행
    elif li[x+1][y]==2:
        x+=1
        li[x][y]=9
        x=8
        y=8
    # 오른쪽 아래 모두 길이 없으면 8,8 리턴
    elif li[x][y+1]==1 and li[x+1][y]==1:
        x=8
        y=8
    return  li,x,y



# 메인 함수 실행 #
def main():
    
    # 박스 생성
    li=[[0 for i in range(10)]for j in range(10)]
    box(li)

    #초기 개미 위치
    x=1
    y=1
    
    #초기 개미 위치 선언
    li[x][y]=9

    while x<9 and y<9:
        #오른쪽 이동 함수 선언
        li,x, y = RIGHT(li,x,y)
        if(li[x+1][y] == 1 and li[x][y+1] == 1):
            break

        #아래 이동 함수 선언
        li,x, y = DOWN(li,x,y)
        if(li[x+1][y] == 1 and li[x][y+1] == 1):
            break
    # 출력 반복문   
    for i in range(len(li)):
        for j in range(len(li)):
            print(li[i][j],end=' ')
        print()

# 메인 함수 동작 로직 #
if __name__=="__main__" :
    main()