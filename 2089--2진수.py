n = int(input())
def decimal(n,k):
    if n == 0:
        return '0'
    else:
        if n % -2 == 0:
            return decimal(n // k, k) + '0'
        else:
            return decimal(n // k+1,k) + '1'
result = decimal(n,-2)
if result == '0':
    print('0')
else:
    print(result[1:])