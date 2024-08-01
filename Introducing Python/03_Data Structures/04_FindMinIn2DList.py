# Problem Statement - Finding minium value in a 2 D list.
matrix = [
    [3, 7, 1, 2],
    [8, 5, 6, 4],
    [2, 1, 8, 9]
]

print(matrix)

min1 = matrix[0][0]
for i in matrix:
    for j in i:
        if min1>j:
            min1 = j
        else:
            min1 = min1

print("Minimum number =",min1)