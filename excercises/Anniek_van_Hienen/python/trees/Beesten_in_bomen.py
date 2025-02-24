# volgende oefening: stop dieren in bomen
# maak een klasse dier
from test.trees.Node import Node
from test.trees.animal_classes import Cat, Dog, Chicken


# creating trees
from test.trees.animal_tree1 import
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


def print_animalsounds(root):
    if root.is_endnode():
        root.get_value().make_sound()
        if isinstance(root.get_value(), Chicken): # verify whether it is a chicken
            root.get_value().lay_egg()
    else:
        print_animalsounds(root.get_left_child())
        print_animalsounds(root.get_right_child())

tree = generate_tree()
print_animalsounds(tree)

# methode overschrijven en een dier maken van een kat, overschrijf parent methode (java: keyword super (=bovenliggende catgeorie aanroepen) en this (=het object wara je nu inzit)
# geef klasse dier een geluid
# maak twee klassen: kat en hond
# klasse dier heeft een methode: maak geluid
# vind geluid van kat en hond

