a,b=input().split()
# 최소
a=a.replace('6','5')
b=b.replace('6','5')
A=int(a)+int(b)
# 최대
a=a.replace('5','6')
b=b.replace('5','6')
B=int(a)+int(b)
print(A,B)