def counttwo(n):
    count = 0
    while n > 0:
        n = n // 5
        count += n
    return count
def countfive(n):
    count = 0
    while n > 0:
        n = n // 2
        count += n
    return count

n, m = map(int, input().split())
print(min(countfive(n)-countfive(m)-countfive(n-m), counttwo(n)-counttwo(m)-counttwo(n-m)))