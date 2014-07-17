# http://www.reddit.com/r/dailyprogrammer/comments/1t0r09/121613_challenge_145_easy_tree_generation/

class PrettyTree(object):
    WIDTH_OF_BASE = 3
    def __init__(self, width, base, limbs):
# This bit sanitizes the width input. Even trees are more work. Can't have that.
        self.width = abs(width)
        while (self.width%2 == 0):
            print "I'm sorry. The program is a little naive. Please enter an odd number:"
            self.width = abs(int(raw_input()))
        self.base = base
        self.limbs = limbs
# As the name suggests, this draws the tree, as specified.
    def draw_Tree(self):
        measure = 1
        height = (self.width + 1)/2 + 1
        # Drawing the limbs:
        for i in range(1,height):
            print ((height - i)*len(self.limbs))*" "+(self.limbs * measure)
            measure += 2
        # Drawing the base:
        print " "*((height - 1)*len(self.limbs))+self.base*self.WIDTH_OF_BASE

# Note: You can input strings, rather than characters for base and limbs. Currently, short
# strings for limbs are more or less supported, but I ran out of time before exactly fixing
# the spacing problem. Strings as the base just get all kinds of ugly. Don't do that.
