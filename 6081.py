a=int(input(),16)
for i in range(1,16,1):
    print('%X'%a,'*%X'%i,'=%X'%(a*i),sep='')