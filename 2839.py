N=int(input())
s=0
for i in range(N//3):
    if((N%5)%3==0):
        s+=N//5
        s+=(N%5)//3
        N=0
        break
    else:
        N=N-3
        s+=1
if(N!=0):
    print(-1)
else:
    print(s)