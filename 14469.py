import sys
input=sys.stdin.readline
N=int(input())
l=[]
for i in range(N):
    l.append(list(map(int, input().split())))
l.sort(key=lambda x:(x[0]))
n=0
for i in range(N):
    if(n<=l[i][0]):
        n=l[i][0]+l[i][1]
    else:
        n=n+l[i][1]
print(n)



# print(l)
# print(type(l))