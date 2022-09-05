# list1=list(map(int, input().split()))
# print(len(list1))
list1=[300,60,10]
s=""
n=int(input())
# for i in range(len(list1)):

# print(n//list1[0])
s+=str(n//list1[0])+" "
n=n%list1[0]
# print("n1:",n)

# print(n//list1[0])
s+=str(n//list1[1])+" "
n=n%list1[1]
# print("n2:",n)

# print(n//list1[0])
s+=str(n//list1[2])+" "
n=n%list1[2]
# print("n3:",n)

if(n==0):
    print(s)
else:
    print("-1")
# print(n//list1[0])
# print(n%list1[0])
# if(n//list1[0]>0):
#     s+=str(n//list1[0])+" "
# print(s)