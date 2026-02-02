# Matrix
# In Python, a matrix is usually represented as a 2D list (a list of lists)

# 1️⃣ Creating a Matrix (2D List)
matrix = [
    [1, 12, 3],
    [44, -52, 6],
    [7, -8, 94]
]
"""
 3 * 3 = 9       first 3 is rows   and    second 3 is columns
 length = 3
 rows = len(matrix)
 columns = len(matrix[0]) """

# 2️⃣ Accessing Elements
print(matrix[0][1])
print(matrix[1][2])

# 3️⃣ Iterating Through a Matrix

#  Row-wise
for row in matrix:
    print(row)

#  Element-wise
for i in range(0,len(matrix)):
    for j in range(0,len(matrix[0])):
        print(matrix[i][j],end=" ")
    print()


# 4️⃣ Taking Matrix Input from User

rows = int(input("Rows: "))
cols = int(input("Cols: "))

nums_matrix = []
for i in range(rows):
    row = list(map(int, input().split()))
    nums_matrix.append(row)

print(nums_matrix)
