
from Node import Node


def generate_tree():
    node1 = Node(1, None, None)
    node2 = Node(2, None, None)
    node3 = Node(None, node1, node2)
    node4 = Node(3, None, None)
    node5 = Node(None, node3, node4)

    print(node5.to_dict())
    return node5

# recursie
# recursie
def get_largest_number(root):
    # ik denk dat dit de basecase is
    if root.is_endnode():
        return root.get_value() # deze geeft de waarde van een eindnode
    else:
        left_child_value = get_largest_number(root.get_left_child()) # deze stopt de left child in de functie
        right_child_value = get_largest_number(root.get_right_child())
        if left_child_value >= right_child_value:
            largest_value_yet = left_child_value
        else:
            largest_value_yet = right_child_value

        return largest_value_yet

print(get_largest_number(generate_tree()))
# stop output in https://jsonformatter.curiousconcept.com/#



print(get_largest_number(generate_tree()))
# stop output in https://jsonformatter.curiousconcept.com/#



# diepte boom
# zou 2 moeten zijn
