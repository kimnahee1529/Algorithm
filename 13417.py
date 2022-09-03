import sys
input=sys.stdin.readline
N=int(input())
list1=[]
list2=[]
for i in range(N):
    n=int(input())
    list1=list(input().split())
    list2.append(list1[0])
    for j in range(n-1):
        if j+1==n:
            break
        else:
            if list1[j+1]<=list2[0]:
                list2.insert(0, list1[j+1])
            else:
                list2.append(list1[j+1])
    print(''.join(list2))
    list1.clear()
    list2.clear()