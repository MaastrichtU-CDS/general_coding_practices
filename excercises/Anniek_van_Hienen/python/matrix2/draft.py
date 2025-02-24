# matrix class
class EmptyMatrix:

    def __init__(self, n_columns, n_rows):
        self.n_columns = n_columns
        self.n_rows = n_rows
        self.matrix = [[]]

        # maak voor iedere rij een lijst gevuld met 0
        for i in range(n_rows):
            row = [0] * n_columns
            self.matrix.append(row)

    def print_matrix(self):
        s = ""
        for x in range(0, len(self.matrix)):
            for y in range(0, len(self.matrix[x])):
                s += str(self.matrix[x][y])
                if y < len(self.matrix[x]) - 1:
                    s += "\t"

            if x < len(self.matrix) - 1:
                s += "\n"  # \n is enter
        return s

m = EmptyMatrix(5, 3)
print(m.print_matrix())

# shape class
class Shape:
    def __init__(self, lengths, rows, offsets):
        self.lengths = lengths # list of number of XX to place in a specific row
        self.rows = rows # list of which rows the XX should be
        self.offsets = offsets # list of starting columns of XX

    def place_line(self, matrix):
        for i in range(len(self.rows)):
            rows = self.rows[i]
            lengths = self.lengths[i]
            offsets = self.offsets[i]

            matrix[rows][offsets:offsets + lengths] = ['X'] * lengths

# application
m= EmptyMatrix(6,5)

shape1 = Shape([3, 2], [2,4], [1, 3])

shape1.place_line(m.matrix)



