N,L=input().split()
N=int(N)
L=int(L)
list1=list(map(int, input().split()))
list1.sort()
for i in range(N):
    if(L>=list1[i]):
        L+=1
    else:
        break
print(L)