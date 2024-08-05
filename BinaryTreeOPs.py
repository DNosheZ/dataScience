class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insertRecursively(self.root, key)
    def _insertRecursively(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self._insertRecursively(root.left, key)
        elif key > root.key:
            root.right = self._insertRecursively(root.right, key)
        return root
    
    #searching methods
    def search(self, key):
        if self._searchRecursively(self.root, key) != None:
            return True
        else:
            return False

    def _searchRecursively(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self._searchRecursively(root.left, key)
        return self._searchRecursively(root.right, key)