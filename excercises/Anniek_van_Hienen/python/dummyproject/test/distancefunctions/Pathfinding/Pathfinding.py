# Matrix class
import copy

class EmptyMatrix:

    value = None

    def __init__(self, n_columns, n_rows):
        self.matrix = []  # Initialize as an empty list
        self.value = None
        # Create a row filled with 0's for each row in the matrix
        for i in range(n_rows):
            row = [0] * n_columns
            self.matrix.append(row)  # Append the row to the matrix/

    # Setting the starting point, using an X and Y coordinate, marked with "s". The coordinates are to be defined later.
    def set_start(self, x, y):
        self.matrix[x][y] = "s"
        self.start_x = x
        self.start_y = y

    # Setting the end point, X and Y coordinate are defined in previous method.
    def set_end(self, x, y):
        self.matrix[x][y] = "e"

    # Added, derived from the Node code, to identify whether this is the end point
    def is_end(self, x, y):
        return self.matrix[x][y] == "e"

    # Added, derived from the Node code, to check the value
    def get_value(self):
        return self.value

    # Added, derived from the Node code, to get the value of the surrounding cells
    def check_left(self, x, y):
        if x-1 >= 0:
            return self.matrix[x-1][y]
        else:
            return "X"

    def check_right(self, x, y):
        if x+1 < len(self.matrix):
            return self.matrix[x+1][y]
        else:
            return "X"

    def check_up(self, x, y):
        if y-1 >= 0:
            return self.matrix[x][y-1]
        else:
            return "X"

    def check_down(self, x, y):
        if y+1 <len(self.matrix[x]):
            return self.matrix[x][y+1]
        else:
            return "X"

    def copy_matrix(self, original_matrix):
        return copy.deepcopy(original_matrix)

    # This method will be used to find a path between s and e
    def padvinden(self, x, y, copy_matrix):
        # relevant variables: s, e, maybe also x and y
        # find out how to use location of s as starting point
        # use decision tree system to find out if neighbouring points are e, X or O
        # something with enumerate to keep track of where we've checked
        ## do not continue if value is X
        ## continue if value is O
        ## task completed if value is e

        # check if current position is end
        if self.is_end(x, y):
            print("Path is found")
            self.print_matrix_inverted()
            print("")
            self.print_matrix_inverted_2(copy_matrix)
            # stop recursion, path is found
            return True

        # Mark this cell as visited
        self.matrix[x][y] = "V"
        copy_matrix[x][y] = "V"

        # find out how to make this loop more efficient, e.g. by changing the check_left/right/... to check whetehr its an X or an s at once

        if self.check_left(x, y) != "X" and self.matrix[x-1][y] != "V":
            print("Left is free, so go to the left")
            if self.padvinden(x-1, y, self.copy_matrix(copy_matrix)):
                return True # If path is found, stop further exploration

        if self.check_right(x,y) != "X" and self.matrix[x+1][y] != "V":
            print("Right is free, so go to the right")
            if self.padvinden(x + 1, y, self.copy_matrix(copy_matrix)):
                return True # If path is found, stop further exploration

        if self.check_up(x, y) != "X" and self.matrix[x][y-1] != "V":
            print("Up is free, so go up")
            if self.padvinden(x, y-1, self.copy_matrix(copy_matrix)):
                return True # If path is found, stop further exploration

        if self.check_down(x, y) != "X" and self.matrix[x][y+1] != "V":
            print("Down is free, so go down")
            if self.padvinden(x, y+1, self.copy_matrix(copy_matrix)):
                return True # If path is found, stop further exploration
        self.matrix[x][y] = "W"
        return False # If no path is found, return False

    # This method prints the empty matrix

    def print_matrix_inverted(self):
        for y in range(len(self.matrix[0])):  # Iterate over columns
            for x in range(len(self.matrix)):  # Iterate over rows for each column
                print(self.matrix[x][y], end=" ")
            print()  # Newline after each inverted row

    def print_matrix_inverted_2(self, matrix):
        for y in range(len(matrix[0])):  # Iterate over columns
            for x in range(len(matrix)):  # Iterate over rows for each column
                print(matrix[x][y], end=" ")
            print()  # Newline after each inverted row

# Shape class
class Shape:
    def __init__(self, lengths, cols, offsets):
        self.lengths = lengths  # List of lists of lengths of X's to place
        self.cols = cols  # List of cols where the X's should be placed
        self.offsets = offsets  # List of lists of starting columns for each segment

    def place_line(self, matrix):
        for i in range(len(self.cols)):
            col = self.cols[i]

            # For each segment in the current row
            for j in range(len(self.lengths[i])):
                length = self.lengths[i][j]
                offset = self.offsets[i][j]

                # Place the X's in the matrix
                matrix[col][offset:offset + length] = ['X'] * length


# Application
if __name__ == "__main__":
    # Create a  matrix
    m = EmptyMatrix(4, 4)

    # Print the initial empty matrix
    print("Initial empty matrix:")
    m.print_matrix_inverted()


    # Create shape using segments
    shape1 = Shape([[1], [1], [0]],
                   [0, 1, 2],
                   [[1], [1], [0]])

    shape2 = Shape([0],
                   [0],
                   [0])
    # Place the shape in the matrix
    shape1.place_line(m.matrix)
    m.set_start(2, 2)
    m.set_end(1, 0)

    # Print the matrix after placing the shape
    print("\nMatrix after placing the barriers:")
    m.print_matrix_inverted()

    m.padvinden(m.start_x, m.start_y, m.copy_matrix(m.matrix))