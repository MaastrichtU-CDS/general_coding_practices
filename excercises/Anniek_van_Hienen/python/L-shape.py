# deze vorm willen we maken
# X X
# X X
# X X
# X X X X X

# is een matrix van 2x4 en dan 3x1

class Map:
    matrix = [[]]
    def __init__(self, row_sizes): # ctrl /
        # self.matrix = [[0 for _ in range(size)] for size in row_sizes] # in binnenste blok: geef mij een lijst van 0 tot lengte
        self.matrix=[]

        for i in range(0, len(row_sizes)):
            self.matrix.append([])
            for j in range(0, row_sizes[i]):
                self.matrix[i].append(0)
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

row_sizes = [2, 2, 2, 5]
m = Map(row_sizes)

print(m.matrix)
print(m.print_matrix())