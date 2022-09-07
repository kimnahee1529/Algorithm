list1=[5,3]
N=int(input())
n=N
s=0
# while(N>3):
#     if((N%5)%3==0):
#         print((N%5)%3==0)
#     elif()
for i in range(n//3):
    if((N%5)%3==0):
        s+=N//5
        # print(s)
        s+=(N%5)//3
        # print(s)
        # if(N==0):
        #     print("break")
        N=0
        break
    else:
        N=N-3
        s+=1
        # print(s)
        
if(N!=0):
    print(-1)
else:
    print(s)