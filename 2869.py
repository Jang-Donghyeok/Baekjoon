import sys
import math
input = sys.stdin.readline

A, B, V = map(int, input().split())
print(math.ceil((V-B)/(A-B)))