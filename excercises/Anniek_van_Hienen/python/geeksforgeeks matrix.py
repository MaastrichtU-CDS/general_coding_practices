Row = int(input("Enter the number of rows:"))
Column = int(input("Enter the number of columns:"))

# make matrix
matrix = []
print("Enter the entries row wise:")

# user input
# for loop for row entries
for row in range(Row):
    a = []
    # for loop for column entries
    for column in range(Column):
        a.append(int(input()))
    matrix.append(a)

# to print the matrix
for row in range(Row):
    for column in range(Column):
        print(matrix[row][column], end="")
    print()

