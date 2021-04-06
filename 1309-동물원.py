n = int(input())
a,b = 1,3
for _ in range(n):
    a,b = b,(2*b+a)%9901
print(a)
