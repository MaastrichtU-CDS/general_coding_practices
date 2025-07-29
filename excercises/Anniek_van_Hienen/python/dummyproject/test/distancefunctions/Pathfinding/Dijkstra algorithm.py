# maak matrixstructuur met nodes en left, right, up, down
print("Initialising maze structure with nodes...")

class Node_Dijkstra:
    left_child = None
    right_child = None
    up_child = None
    down_child = None

    distance_to_leftchild = None
    distance_to_rightchild = None
    distance_to_upchild = None
    distance_to_downchild = None

    value = None

    def __init__(self, value, left_child, distance_to_leftchild, right_child, distance_to_rightchild, up_child, distance_to_upchild, down_child, distance_to_downchild): # dit is een constructor
        self.left_child = left_child
        self.right_child = right_child
        self.up_child = up_child
        self.down_child = down_child

        self.distance_to_leftchild = distance_to_leftchild
        self.distance_to_rightchild = distance_to_rightchild
        self.distance_to_upchild = distance_to_upchild
        self.distance_to_downchild = distance_to_downchild

        self.value = value

    def get_value(self):
        return self.value

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def get_up_child(self):
        return self.up_child

    def get_down_child(self):
        return self.down_child

    def get_distance_to_leftchild(self):
        return self.distance_to_leftchild

    def get_distance_to_rightchild(self):
        return self.distance_to_rightchild

    def get_distance_to_upchild(self):
        return self.distance_to_upchild

    def get_distance_to_downchild(self):
        return self.distance_to_downchild

    def is_endnode(self):
        return self.value != None

    def to_dict(self):
        return {
            'value': self.value,

            'left_child': self.left_child.to_dict() if self.left_child else None,
            'right_child': self.right_child.to_dict() if self.right_child else None,
            'up_child': self.up_child.to_dict() if self.up_child else None,
            'down_child': self.down_child.to_dict() if self.down_child else None,

            'distance_to_leftchild': self.distance_to_leftchild.to_dict() if self.distance_to_leftchild else None,
            'distance_to_rightchild': self.distance_to_rightchild.to_dict() if self.distance_to_rightchild else None,
            'distance_to_upchild': self.distance_to_upchild.to_dict() if self.distance_to_upchild else None,
            'distance_to_downchild': self.distance_to_downchild.to_dict() if self.distance_to_downchild else None,
        }

def_generate_maze(self):
    Node_A = Node_Dijkstra(None, "Node_B", "Node_C, None, None)
    Node_B = Node_Dijkstra("s", "Node_C", 5, None, None, 

print("Maze created")

## maak lijsten
print("Creating lists with visited and unvisited nodes")

unvisited_nodes = []
visited_nodes = []

print("Lists created")