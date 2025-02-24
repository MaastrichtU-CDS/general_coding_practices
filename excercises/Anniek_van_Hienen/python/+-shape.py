#     0
#     0
# 0 0 0 0 0
#     0
#     0

class Map:
    matrix = [[]]
    def __init__(self, row_sizes, empty_first_column_rows):
        self.matrix = []
        for i, size in enumerate(row_sizes): # enumerate gaat door het lijstje
            if i in empty_first_column_rows:
                self.matrix.append([None] + [0 for j in range(size-1)] if size > 0 else [])
            else:
                self.matrix.append([0 for j in range(size)] if size > 0 else [])

    def print_matrix(self):
        s = ""
        for x in range(0, len(self.matrix)):
            for y in range(0, len(self.matrix[x])):
                value = self.matrix[x][y]
                s += str(value) if value is not None else " "
                if y < len(self.matrix[x])-1:
                    s+= "\t"

            if x < len(self.matrix)-1:
                s += "\n" # \n is enter
        return s

row_sizes = [3, 3, 3]
empty_first_column_rows = [1]
m = Map(row_sizes, empty_first_column_rows)

print(m.matrix)
print(m.print_matrix())