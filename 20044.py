N=int(input())
list1=list(map(int, input().split()))
list2=[]
big_list=sorted(list1, reverse=True)
small_list=sorted(list1)
for i in range(N):
    list2.append(small_list[i]+big_list[i])
print(min(list2))
