def pivoting(mat):
    row_idx = list(range(len(mat)))
    col_idx = len(mat[0])
    pivot_mat = []
    for c in range(col_idx):
        rows_with_nonzero = [r for r in row_idx if mat[r][c] != 0]
        if rows_with_nonzero:
            pivot = rows_with_nonzero[0]
            for idx in rows_with_nonzero:
                pivot_mat.append(mat[idx])
                row_idx.remove(idx)
    return pivot_mat

A = [[3, 2, -1, -15],
       [5, 3, 2, 0],
       [3, 1, 3, 11],
       [6, -4, 2, 30]]
from pprint import pprint
pprint(pivoting(A))
