import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    score = 0
    result = 0
    quiz = input()
    for j in range(len(quiz)):
        if quiz[j] == 'O':
            score += 1
        else:
            score = 0
        result += score
    print(result)