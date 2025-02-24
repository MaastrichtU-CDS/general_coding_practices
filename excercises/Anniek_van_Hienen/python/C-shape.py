class Map:
    matrix = [[]]
    def __init__(self, row_sizes):
        self.matrix = [[0 for _ in range(size)] for size in row_sizes] # in binnenste blok: geef mij een lijst van 0 tot lengte

    def print_matrix(self):
        s = ""
        for x in range(0, len(self.matrix)):
            for y in range(0, len(self.matrix[x])):
                s += str(self.matrix[x][y])
                if y < len(self.matrix[x])-1:
                    s+= "\t"

            if x < len(self.matrix)-1:
                s += "\n" # \n is enter
        return s

row_sizes = [4, 2, 1, 2, 4]
m = Map(row_sizes)

print(m.matrix)
print(m.print_matrix())