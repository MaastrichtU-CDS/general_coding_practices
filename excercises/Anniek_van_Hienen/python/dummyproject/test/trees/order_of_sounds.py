# bouw een boom waarin je in een specifieke volgorde geluiden uitprint --> inzihct ontwikkelen
# maak wat verschillende bomen

# make classes
class Sound:
    # this is a class
    def __init__(self):
        pass
    def make_sound(self):
        print("I make a sound!")

class Guns(Sound):
    def make_sound(self):
        print("pew")


class Crash(Sound):
    def make_sound(self):
        print("boom")

class DroppingStuff(Sound):
    def make_sound(self):
        print("bang")


# make trees
from test.trees.Node import Node
def generate_tree():
    guns = Guns()
    crash = Crash()
    dropping_stuff = DroppingStuff()

    Node1= Node(guns, None, None)
    Node2= Node(crash, None, None)
    Node3= Node(None, Node1, Node2)
    Node4= Node(dropping_stuff, None, None)
    Node5= Node(None, Node3, Node4)

    return Node5
# pew, boom, bang
tree = generate_tree()

# function to go through tree and print sounds
def play_sound(root):
    #base case
    if root is None:
        return "error"
    if root.is_endnode(): # method requires brackets to be called
        root.get_value().make_sound()
    else:
        left = play_sound(root.get_left_child())
        right = play_sound(root.get_right_child())


play_sound(tree)


