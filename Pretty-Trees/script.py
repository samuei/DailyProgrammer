# http://www.reddit.com/r/dailyprogrammer/comments/1t0r09/121613_challenge_145_easy_tree_generation/

class PrettyTree(object):
    def __init__(self, width, base, limbs):
        self.width = abs(width)
        while (self.width%2 == 0):
            print "I'm sorry. The program is a little naive. Please enter an odd number:"
            self.width = abs(int(raw_input()))
        self.base = base
        self.limbs = limbs
    def draw_Tree(self):
        measure = 1
        height = (self.width + 1)/2 + 1
        for i in range(1,height):
            print (height - i)*" "+(self.limbs * measure)
            measure += 2
        print " "*(height - 2)+self.base*3
