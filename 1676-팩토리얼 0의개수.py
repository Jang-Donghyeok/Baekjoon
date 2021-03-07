n = int(input())
fac = 1
count = 0
for i in range(1, n+1):
    fac *= i
fac = str(fac)
i = -1
while int(fac[i]) == 0:
    count += 1
    i -= 1
print(count)