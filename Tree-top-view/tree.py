class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""


def topView(root, hd, m):
    # Write your code here
    if root == None:
        return
    else:
        if hd not in m.keys():
            m[hd] = root.info
        if root.left:
            topView(root.left, hd-1, m)
        if root.right:
            topView(root.right, hd+1, m)
    return m


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])
m = {}
hd = 0
l = topView(tree.root, hd, m)
ok = list(l.keys())
ok.sort()

#print(ok)

for key in ok:
    print(l[key], end= " ")
