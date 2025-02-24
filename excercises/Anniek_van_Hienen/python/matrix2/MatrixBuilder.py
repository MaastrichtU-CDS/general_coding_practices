class MatrixBuilder:
    matrix = [[]]
    length = None # hoeveel X'en op een rij worden geprint
    column = None #
    row = None # in welke rij deze worden geprint
    offset = None # hoe ver de rij X'en naar rechts wordt opgeschoven

    def __init__(self, length, row, column, offset):
        self.length = length
        self.column = column
        self.row = row
        self.offset = offset

        for i in range(0, len(column)):
            self.matrix.append([])
            for j in range(0, column[i]):
                self.matrix[i].append(0)

        def get_length(self):
            return self.length

        def get_column(self):
            return self.column

        def get_row(self):
            return self.row

        def get_offset(self):
            return self.offset

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




MatrixBuilder(3,4,5, 1)