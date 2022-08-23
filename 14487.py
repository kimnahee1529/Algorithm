# 리스트에 정수를 입력받는 게 처음엔 헷갈렸음
# 띄어쓰기로 입력받으려면 for문 X, 엔터로 입력받을 때 for문을 써야 함
n=list(map(int, input().split()))
print(n)
print(max(n))
n.remove(max(n))
print(sum(n))
