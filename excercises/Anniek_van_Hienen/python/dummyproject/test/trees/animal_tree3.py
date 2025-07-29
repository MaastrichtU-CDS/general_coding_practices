# import pickle to save the tree
import pickle

# import Node object and animals to create a tree
from test.trees.Node import Node
from test.trees.animal_classes import Cat, Dog, Chicken

def generate_tree():
    cat = Cat()
    dog1 = Dog()
    dog2 = Dog()
    dog3 = Dog()
    chicken = Chicken()

    node1 = Node(chicken, None, None)
    node2 = Node(dog1, None, None)
    node3 = Node(cat, None, None)
    node4 = Node(dog3, None, None)
    node5 = Node(dog2, None, None,)
    node6 = Node(None, node1, node2)
    node7 = Node(None, node6, node3)
    node8 = Node(None, node4, node7)
    node9 = Node(None, node8, node5)

    return node9

tree = generate_tree()

# save the tree object
with open('animal_tree3.pkl', 'wb') as file:
    pickle.dump(tree, file)

print("animal_tree3 object saved.")