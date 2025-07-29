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



