# http://www.reddit.com/r/dailyprogrammer/comments/1t0r09/121613_challenge_145_easy_tree_generation/

class PrettyTree(object):
    """ An object for building pretty trees """
    WIDTH_OF_BASE = 3
    # The base's width is constant due to project specs.
    
    def __init__(self, width, base, limbs):
        """
        Width = Width of bottom row of tree limbs.
        Base = Character that the tree's trunk will be made of (single character only).
        Limbs = String that the tree's limbs will be made of (longer strings allowed).
        Note: Even-length limb strings will result in an ugly tree. I won't stop you,
              but you're going to have to live with your ugly tree, Charlie Brown.
        """
        # This bit sanitizes the width input. Even trees are ugly. Can't have that.
        self.width = abs(width)
        while (self.width%2 == 0):
            self.width = abs(int(raw_input("I'm sorry. The program is a little naive. Please enter an odd number:")))
        self.base = base
        # This bit sanitizes the base input.
        while (len(self.base) > 1):
            self.base = raw_input("I'm sorry, but the base can't have more than one character. Please enter a single character:")
        self.limbs = limbs
    
    def draw_Tree(self):
        """ This prints the pretty tree """
        measure = 1
        height = (self.width + 1)/2 + 1
        # Drawing the limbs:
        for i in range(1,height):
            print ((height - i)*len(self.limbs))*" "+(self.limbs * measure)
            measure += 2
        # Drawing the base:
        print " "*(((height - 1)*len(self.limbs))+((len(self.limbs)-self.WIDTH_OF_BASE)/2))+self.base*self.WIDTH_OF_BASE
