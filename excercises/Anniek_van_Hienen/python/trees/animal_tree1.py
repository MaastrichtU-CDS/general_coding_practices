# import pickle to save the tree
import pickle

# import Node object and animals to create a tree
from test.trees.Node import Node
from test.trees.animal_classes import Cat, Dog, Chicken

def generate_tree():
    cat = Cat()
    dog1 = Dog()
    chicken = Chicken()

    node1 = Node(cat, None, None)
    node2 = Node(dog1, None, None)
    node3 = Node(None, node1, node2)
    node4 = Node(chicken, None, None)
    node5 = Node(None, node3, node4)

    return node5

tree = generate_tree()

# save the tree object
with open('animal_tree1.pkl', 'wb') as file:
    pickle.dump(tree, file)

print("animal_tree1 object saved.")