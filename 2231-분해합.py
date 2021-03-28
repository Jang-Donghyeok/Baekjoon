mat = [[3,2,-1],[5,3,2],[3,1,3],[6,-4,2]]
c = [-15,0,11,30]
for i in range(len(mat)):
    print(mat[i])
for i in range(len(c)):
    print(" "+ str(c[i]))

for i in range(len(mat)):
    mat[i].append(c[i])

mat = sorted(mat, key= lambda x: abs(x[0]), reverse=True)

for pivot in range(4):
    for y in range(0,4):