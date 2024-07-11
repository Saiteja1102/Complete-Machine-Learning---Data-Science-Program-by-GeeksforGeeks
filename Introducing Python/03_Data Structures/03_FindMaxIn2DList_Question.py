# Problem Statement - Finding maximum value in a 2 D list.
matrix = [
    [3, 7, 1, 2],
    [8, 5, 6, 4],
    [2, 1, 8, 9]
]

print(matrix)

max = 0
for i in matrix:
    for j in i:
        if (j > max):
            max = j
        else:
            max = max

print("Maximum number = ",max)