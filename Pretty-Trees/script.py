# http://www.reddit.com/r/dailyprogrammer/comments/1t0r09/121613_challenge_145_easy_tree_generation/

class PrettyTree(object):
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
            print (height - i)*" "+(self.limbs * measure)
            measure += 2
        # Drawing the base:
        print " "*(height - 2)+self.base*3

# Note: You can input strings, rather than characters for base and limbs, but the spaces won't format correctly.
# That's fixable by factoring in the len() of the relevant one in each place, but the user shouldn't be messing
# with my beautiful character trees like that, anyway.
