class Node():
    def __init__(self,d, n=None):
        self.data = d
        self.next = n

    def get_next(self):
        return self.next

    def set_next(self, n):
        self.next = n #set next node

    def get_data(self):
        return self.data

    def set_data(self,d):
        self.data = d

class Linkedlist:
    def __init__(self, r=None):
        self.root = r
        if self.root == None:
            self.size = 0
        else:
            self.size = 1

    def get_size(self):
        return self.size

    def add(self, d): #add new node in the beginning
        if self.root == None:
            self.root = Node(d)
        else:
            node = Node(d, self.root)
            self.root = node
        self.size = self.size + 1

    def find(self, d):
        node = self.root #start fom the root node
        while node.get_next() is not None:
            if node.get_data() == d:
                return True
            elif node.get_next() == None: #we are at the last of the linked list
                return False
            else:
                node = node.get_next()

    def remove(self, d):
        node = self.root
        prev = None

        while node.get_next() is not None:
            if node.get_data() == d:
                if prev is not None:
                    prev.set_next(node.get_next())
                else:
                    self.root.set_next(node.get_next())
                self.size = self.size - 1
                return True
            else:
                prev = node
                node = node.get_next()
        if node.get_next() is None and node.data == d: # if element to be removed is the last element
            prev.next = None
            return True
        return False

    def display(self):
        node = self.root

        while node.next is not None:
            print(node.data, end=" ")
            node = node.next
        if node.next is None:
            print(node.data , end = " ")
        print("\n")

def main():
    n = Node(5)
    l = Linkedlist(n)
    l.add(10)
    l.add(15)
    l.add(8)
    l.display()
    l.remove(5)
    l.display()


main()
