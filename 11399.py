list1=[]
N=int(input())
s=0
n=list(map(int, input().split()))
n=sorted(n)
# print(n)
for i in range(N):
    s+=n[i]
    list1.append(s)
print(sum(list1))
    