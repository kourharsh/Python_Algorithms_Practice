class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree():
    def __init__(self, root):
        self.root = root

    def levelorder(self):
        order = []
        if self.root is not None:
            queue = []
            queue.append(self.root)
            while(len(queue) > 0):
                first = queue.pop(0)
                #print(first.data)
                order.append(first.data)
                if first.left:
                    queue.append(first.left)
                if first.right:
                    queue.append(first.right)
        return order

    def preorder(self):
        order = []
        if self.root is not None:
            stack = []
            stack.insert(0,self.root)
            while(len(stack) > 0):
                first = stack.pop(0)
                order.append(first.data)
                if first.right: #right  inserted first so that while pop from stack left will be processed first
                    stack.insert(0, first.right)
                if first.left:
                    stack.insert(0, first.left)
        return order

    def inorder(self): #stack root and set it as current, if current.left then stack it and make current.left as current
        #if current is Null, pop stack and print and current is current.right
        order = []
        if self.root is not None:
            stack = []
            current = self.root
            while True:
                if current is not None:
                    stack.insert(0, current)
                    current = current.left
                elif stack:
                    s = stack.pop(0)
                    order.append(s.data)
                    current = s.right
                else:
                    break

        return order

    def postorder(self):
        order = []
        if self.root is not None:
            stack = []
            current = self.root
            visited = []
            while current and current not in visited:
                if current.left and current.left not in visited:
                    current = current.left
                elif current.right and current.right not in visited:
                    current = current.right
                else:
                    order.append(current.data)
                    visited.append(current)
                    current = self.root


        return order



#           1
#         /   \
#        2     3
#       / \   / \
#      4   5  6  7

t = Tree(Node(1))
t.root.left = Node(2)
t.root.right = Node(3)
t.root.left.left = Node(4)
t.root.left.right = Node(5)
t.root.right.left = Node(6)
t.root.right.right = Node(7)
order = t.levelorder()
print(order)
order = t.preorder()
print(order)
order = t.inorder()
print(order)
order = t.postorder()
print(order)