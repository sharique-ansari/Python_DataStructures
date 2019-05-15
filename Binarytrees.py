# full implementation of binary tree data structure with all necessary functions


class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


    def insert(self,data):
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



if __name__ == "__main__":
    tree = Node(3)
    tree.insert(4)
    tree.insert(2)
    tree.insert(9)
    tree.insert(1)
    tree.printtree()

#     below is the example tree
#           3
#       2         4
#   1                 9


