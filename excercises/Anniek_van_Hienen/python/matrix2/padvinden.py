# Matrix class
class EmptyMatrix:
    start_x = -1
    start_y = -1

    def __init__(self, n_columns, n_rows):
        self.matrix = []  # Initialize as an empty list
        # Create a row filled with 0's for each row in the matrix
        for i in range(n_rows):
            row = [0] * n_columns
            self.matrix.append(row)  # Append the row to the matrix

    def set_start(self, x, y):
        self.matrix[x][y] = "s"
        self.start_x = x
        self.start_y = y

    def set_end(self, x, y):
        self.matrix[x][y] = "e"

    def padvinden(self):
        self.start_x
        self.start_y
        # aanp

    def print_matrix(self):
        s = ""
        for x in range(len(self.matrix)):
            for y in range(len(self.matrix[x])):
                s += str(self.matrix[x][y])
                if y < len(self.matrix[x]) - 1:
                    s += "\t"  # Add a tab between elements

            if x < len(self.matrix) - 1:
                s += "\n"  # Add a newline after each row
        return s


# Shape class
class Shape:
    def __init__(self, lengths, rows, offsets):
        self.lengths = lengths  # List of lists of lengths of X's to place
        self.rows = rows  # List of rows where the X's should be placed
        self.offsets = offsets  # List of lists of starting columns for each segment

    def place_line(self, matrix):
        for i in range(len(self.rows)):
            row = self.rows[i]

            # For each segment in the current row
            for j in range(len(self.lengths[i])):
                length = self.lengths[i][j]
                offset = self.offsets[i][j]

                # Place the X's in the matrix
                matrix[row][offset:offset + length] = ['X'] * length


# Application
if __name__ == "__main__":
    # Create a 5x5 matrix
    m = EmptyMatrix(5, 5)

    # Print the initial empty matrix
    print("Initial empty matrix:")
    print(m.print_matrix())

    # Create shape using segments
    shape1 = Shape([[5], [1, 1], [1, 1], [1, 1], [5]],
                   [0, 1, 2, 3, 4],
                   [[0], [0, 4], [0, 4], [0, 4], [0]])

    shape2 = Shape([[1], [1], [5], [1], [1]],
                   [0, 1, 2, 3, 4],
                   [[2], [2], [0], [2], [2]])
    # Place the shape in the matrix
    shape2.place_line(m.matrix)
    m.set_start(1,1)
    m.set_end(4,4)

    # Print the matrix after placing the shape
    print("\nMatrix after placing the 'O' shape:")
    print(m.print_matrix())
