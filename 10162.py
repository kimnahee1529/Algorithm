list1=[300,60,10]
s=""
n=int(input())

s+=str(n//list1[0])+" "
n=n%list1[0]

s+=str(n//list1[1])+" "
n=n%list1[1]

s+=str(n//list1[2])+" "
n=n%list1[2]

if(n==0):
    print(s)
else:
    print("-1")