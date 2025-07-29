# vind de positie van de hond in de boom
# als twee honden: vind positie van minst diepe hond
# als er geen hond is, geef -99 terug
# mogelijk met combineren dit script (beesten en bomen) met dieptes vinden in vorige
# bouw een boom waarin je in een specifieke volgorde geluiden uitprint --> inzihct ontwikkelen
# maak wat verschillende bomen

# import prerequisites
import pickle
from test.trees.Node import Node
from test.trees.animal_classes import Cat, Dog, Chicken

# import tree 1
with open('animal_tree3.pkl', 'rb') as file:
    tree = pickle.load(file)

# create new function
def find_dog(root, depth):
    if depth is None:
        depth = 1
    # base case
    if root is None:
        return 999

    if root.is_endnode() and isinstance(root.get_value(), Dog):
        return depth

    else:
        left_depth = find_dog(root.get_left_child(), depth + 1)  # deze stopt de left child in de functie
        right_depth = find_dog(root.get_right_child(), depth + 1)

        return min(left_depth, right_depth)

dog_depth = find_dog(tree, None )
if dog_depth == 999:
    print("No dogs found in the tree.")
else:
    print(f"The lowest depth where a Dog is found: {dog_depth}")



