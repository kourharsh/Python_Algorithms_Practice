#!/bin/python3

import os
import sys


class Node:
    def __init__(self, data, level):
        self.data = data
        self.left = None
        self.right = None
        self.level = level

    def insert(self, val):  # inserting tree in level order
        queue = []
        queue.append(self)
        while (len(queue) != 0):
            first = queue[0]
            queue.pop(0)
            if first.left == None:
                first.left = Node(val, first.level + 1)
                break
            elif first.left.data != -1:
                queue.append(first.left)
            if first.right == None:
                first.right = Node(val, first.level + 1)
                break
            elif first.right.data != -1:
                queue.append(first.right)


def inorder(root, s):
    if root == None:
        return
    if root.left:
        inorder(root.left, s)
    if root.data != -1:
        s.append(root.data)
    # print(root.data, end=" ")
    if root.right:
        inorder(root.right, s)
    return s


# Complete the swapNodes function below.
#
def removeNodes():
    queue = []
    queue.append(self)
    while (len(queue) != 0):
        first = queue[0]
        queue.pop(0)
        if first.data == -1:
            first = None
        else:
            if first.left:
                queue.append(first.left)
            if first.right:
                queue.append(first.right)


def swapNodes(root, k):
    #
    # Write your code here.
    #
    queue = []
    queue.append(root)
    while (len(queue) != 0):
        f = queue[0]
        # print("f is " + str(f.data))
        queue.pop(0)
        if (f.level) % k == 0 and f.left and f.right:
            f.left, f.right = f.right, f.left
        if f.left:
            queue.append(f.left)
        if f.right:
            queue.append(f.right)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    # print(n)

    indexes = []

    root = Node(1, 1)
    for i in range(0, n):
        # ndexes.append(list(map(int, input().rstrip().split())))
        a = input().rstrip().split(" ")
        # print(a)
        a1 = int(a[0])
        b1 = int(a[1])
        root.insert(a1)
        root.insert(b1)
        # root.insert_n(a1,b1)

    s = []
    # m = inorder(root, s)
    # print(m)

    queries_count = int(input())

    queries = []

    # arr = np.zeros((queries_count, n))

    for j in range(0, queries_count):
        k = int(input())
        # print("k is -- " + str(k))
        swapNodes(root, k)
        # removeNodes(root)
        s = []
        m = inorder(root, s)
        # print(m)
        # arr[j] =m
        # print(arr)
        s = ""
        for key in m:
            s = s + str(key) + " "

        fptr.write(s)
        fptr.write('\n')

    fptr.close()
