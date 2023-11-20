from math import ceil, floor


class Node:
    def __init__(self, v, parent=None, depth=0):
        self.val = None
        self.l = None
        self.r = None
        self.parent = parent
        self.depth = depth
        if isinstance(v, int):
            self.val = v
        else:
            l, r = v
            self.l = Node(l, self, depth+1)
            self.r = Node(r, self, depth+1)

    def __repr__(self):
        if self.val is not None:
            return str(self.val)
        return f'[{self.l},{self.r}]'
    
    def __add__(self, other):
        return Node(eval(f'[{self},{other}]'))
    
    def explode(self):
        node = self
        left_node = None
        done = False
        while not done:
            if node.val is None:
                if node.depth == 4:
                    break
                node = node.l
            else:
                left_node = node
                while node.parent.r is node:
                    node = node.parent
                    if node.parent is None:
                        done = True
                        break
                if not done:
                    node = node.parent.r
        
        if done:
            return False
        
        right_node = node
        while right_node.parent.r is right_node:
                right_node = right_node.parent
                if right_node.parent is None:
                    right_node = None
                    break
        if right_node is not None:
            right_node = right_node.parent.r
            while right_node.val is None:
                right_node = right_node.l

        if left_node is not None:
            left_node.val += node.l.val
        if right_node is not None:
            right_node.val += node.r.val

        node.l = None
        node.r = None
        node.val = 0
        return True

    def split(x):
        if x.val is None:
            return x.l.split() or x.r.split()
        if x.val >= 10:
            l = int(floor(x.val/2))
            r = int(ceil(x.val/2))
            x.val = None
            x.l = Node(l, x, x.depth+1)
            x.r = Node(r, x, x.depth+1)
            return True
        return False

    def magnitude(self):
        if self.val is not None:
            return self.val
        return 3 * self.l.magnitude() + 2 * self.r.magnitude() 

    def reduce(self):
        while True:
            if self.explode():
                continue
            if not self.split():
                break
        return self

def solve(f):
    s = None
    for line in open(f).read().splitlines():
        n = Node(eval(line.strip()))
        if s is not None:
            s = s + n
            s.reduce()
        else:
            s = n
    return s.magnitude()
        

def solve2(f):
    nodes = []
    for line in open(f).read().splitlines():
        nodes.append(Node(eval(line.strip())))

    best = 0
    for i in range(len(nodes)):
        for j in range(len(nodes)):
            if i == j:
                continue
            mag = (nodes[i] + nodes[j]).reduce().magnitude()
            best = max(best, mag)
    
    return best
    

if __name__ == '__main__':
    # print(solve('18_test.txt'))
    print(solve('18.txt'))
    # print(solve2('18_test.txt'))
    print(solve2('18.txt'))
