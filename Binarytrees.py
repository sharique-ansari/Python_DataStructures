# full implementation of binary tree data structure with all necessary functions


class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

    def insert(self, data):
        if self.val:
            if self.val < data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
            elif self.val > data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
        else:
            self.val = data

    def printtree(self):
        if self.left:
            self.left.printtree()
        print(self.val)
        if self.right:
            self.right.printtree()

    def findintree(self, fval):
        if fval < self.val:
            if self.left is None:
                return "Given value does not exist in tree:" + str(fval)
            return self.left.findintree(fval)
        elif fval > self.val:
            if self.right is None:
                return "Given value does not exist in tree:" + str(fval)
            return self.right.findintree(fval)
        else:
            return str(fval) + " is found."

    def minBST(self):
        if self.left is None:
            return self
        return self.left.minBST()

    def delete(self, dval):
        if self is None:
            return self
        if dval < self.val:
            self.left = self.left.delete()
        elif dval > self.val:
            self.right = self.right.delete()
        else:
            if self.left is None:
                temp = self.right
                self = None
                return temp
            elif self.right is None:
                temp = self.left
                self = None
                return temp
            temp = self.right.minBST()
            self.val = temp.val
            self.right = self.right.delete(temp.val)

    def getHeight(self,root):
        if root is None:
            return -1
        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))


if __name__ == "__main__":
    tree = Node(3)
    tree.insert(4)
    tree.insert(2)
    tree.insert(9)
    tree.insert(1)
    tree.printtree()

    print(tree.findintree(89))
    print(tree.findintree(9))
    print(tree.getHeight(tree))

    # tree.delete(3)
    # tree.printtree()

#     below is the example tree
#           3
#       2         4
#   1                 9
