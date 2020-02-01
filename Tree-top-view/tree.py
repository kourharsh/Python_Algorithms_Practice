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


def levelordertraversal(root):
    s = []
    listqueue = []
    listqueue.append(root)
    while (len(listqueue) != 0):
        first = listqueue[0]
        listqueue.remove(first)
        s.append(first.info)
        if first.left:
            listqueue.append(first.left)
        if first.right:
            listqueue.append(first.right)
    return s


def topView_h(root, hd, m):
    # Write your code here
    if root == None:
        return
    else:
        if hd not in m.keys():
            m[hd] = [root.info]
        else:
            l = m[hd]
            l.append(root.info)
            m[hd] = l
        if root.left:
            topView_h(root.left, hd - 1, m)
        if root.right:
            topView_h(root.right, hd + 1, m)
    return m


def topView(root):
    s = levelordertraversal(root)
    # print(s)
    m = {}
    hd = 0
    l = topView_h(root, hd, m)
    # print(l)
    ok = list(l.keys())
    ok.sort()
    # print(l)
    for key in ok:
        l_list = l[key]
        index = 999999999999
        elem = 0
        for i in l_list:
            i_current = s.index(i)
            # print(i_current)
            if i_current < index:
                index = i_current
                elem = i
        print(elem, end=" ")


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

topView(tree.root)