class Node:
    left_child = None
    right_child = None
    value = None

    def __init__(self, value, left_child, right_child): # dit is een constructor
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

    def get_value(self):
        return self.value

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def is_endnode(self):
        return self.value != None

    def to_dict(self):
        return {
            'value': self.value,
            'left_child': self.left_child.to_dict() if self.left_child else None,
            'right_child': self.right_child.to_dict() if self.right_child else None,
        }

# decision tree part
from Node import Node


def generate_tree():
    node11 = Node(3, None, None)
    node10 = Node(1, None, None)
    node9 = Node(3, None, None)
    node8 = Node(2, None, None)
    node5 = Node(None, node10, node11)
    node4 = Node(None, node8, node9)
    node3 = Node(1, None, None)
    node2 = Node(None, node4, node5)
    node1 = Node(None, node2, node3)

    print("This node has the following content: ", node1.to_dict())
    return node1



# maximale diepte boom
# zou 2 moeten zijn
# in plaats van de waarde teruggeven, nu dus de diepte teruggeven. vergelijkbare logica.
# minimale diepte
# grootste waardeop diepte D: kijken naar grootste node, waarde, en de diepte.

def get_depth(root):
    if root is None:
        return 0
    elif root.is_endnode():
        return 1
    else:
        depth_left = get_depth(root.get_left_child())
        depth_right = get_depth(root.get_right_child())
        if depth_left >= depth_right:
            return depth_left + 1
        else:
            return depth_right + 1

print("The depth of this tree is", get_depth(generate_tree()))


# vind de minste diepe van een bepaalde waarde (bv. 5)
# stap 1: pas boom aan zodat er meerdere keren dezelfde waarde inzet
# stap 2: weer met recursie bezig gaan

def get_minimal_depth(root:Node, value: int = 2):
    if root is None:
        return 0

    elif root.is_endnode() and root.value == value:
        return 1

    elif root.is_endnode() and not root.value == value:
        return 0

    else:
        min_depth_left = get_minimal_depth(root.get_left_child(), value)
        min_depth_right = get_minimal_depth(root.get_right_child(), value)

        if min_depth_left <= min_depth_right:
            return min_depth_left + 1

        else:
            return min_depth_right + 1

print("The minimal depth of the value of interest in this tree is", get_minimal_depth(generate_tree()))

# gpt
def get_minimal_depth(root: Node, value: int = 2):
    if root is None:
        return float('inf')  # Large number indicating the value is not found in this path

    if root.is_endnode() and root.value == value:
        return 1

    # Recursively find the minimal depth in both subtrees
    min_depth_left = get_minimal_depth(root.get_left_child(), value)
    min_depth_right = get_minimal_depth(root.get_right_child(), value)

    # Return the minimum depth found in either subtree plus one for the current node
    return min(min_depth_left, min_depth_right) + 1

print("The minimal depth of the value of interest in this tree is", get_minimal_depth(generate_tree()))