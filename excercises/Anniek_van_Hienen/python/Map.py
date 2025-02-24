class Map:
    matrix = [[]]
    def __init__(self, width, length):
        self.matrix = [[0 for _ in range(width)] for _ in range(length)] # in binneste blok: geef mij een lijst van 0 tot lengte
        print(self.matrix)

    def set_start(self, x, y):
        self.matrix[x][y] = "s"

    def set_end(self, x, y):
        self.matrix[x][y] = "e"

    def set_wall(self, x, y):
        self.matrix[x][y] = "w"

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



m = Map(4, 5)

m.set_start(0, 2) # programmeurs beginnen met tellen bij 0!!!
m.set_end(3, 3)
m.set_wall(1,2)
m.set_wall(0,1)

print(m.matrix)
print(m.print_matrix())