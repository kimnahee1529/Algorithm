# 조건문이 너무 많아서 다시 생각함! 그리고 맞은 건 아님ㅋ
# T=int(input())
# S=''
# a,b,c,d=25,10,5,1
# # print(a)
# for i in range(T):
#     N=int(input())
#     if(N>a):
#         S+=str(N//a)+' '
#         N=N%a
#         print(S)
#         print(N)
#     if(N>b):
#         S+=str(N//b)+' '
#         N=N%b
#         print(S)
#         print(N)
#     if(N>c):
#         S+=str(N//c)+' '
#         N=N%c
#         print(S)
#         print(N)
#     if(N>d):
#         S+=str(N//d)+' '
#         N=N%d
#         print(S)
#         print(N)
    
T=int(input())
S=''
list1=[25,10,5,1]
list2=[]
for i in range(T):
    N=int(input())
    for i in range(4):
        list2.append(str(N//list1[i]))
        N=N%list1[i]
for i in range(1,T+1):
    print(' '.join(list2[(i-1)*4:i*4]))
    