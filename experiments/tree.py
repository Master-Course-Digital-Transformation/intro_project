class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if self.value is None:
            self.value = value
        else:
            if value < self.value:
                if self.left is None:
                    self.left = BinaryTree(value)
                else:
                    self.left.insert(value)
            else:
                if self.right is None:
                    self.right = BinaryTree(value)
                else:
                    self.right.insert(value)
    
    def is_in_tree(self, value):
        if value == self.value:
            return True
        if value < self.value:
            if self.left is None:
                return False
            return self.left.is_in_tree(value)
        else:
            if self.right is None:
                return False
            return self.right.is_in_tree(value)
        
    def __str__(self):
        return f"{self.value} \ {self.left} / {self.right}"
    
if __name__ == "__main__":
    tree = BinaryTree(5)
    tree.insert(3)
    tree.insert(8)
    tree.insert(2)
    tree.insert(4)
    tree.insert(7)
    tree.insert(9)
    print(tree)
    print(tree.is_in_tree(3))
    print(tree.is_in_tree(10))
    print(tree.is_in_tree(7))
    print(tree.is_in_tree(2))
    print(tree.is_in_tree(5))
    print(tree.is_in_tree(9))