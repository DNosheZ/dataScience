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
    
    def height(self):
        return self._heightRecursively(self.root)

    def _heightRecursively(self, root):
        if root is None:
            return 0
        else:
            left_height = self._heightRecursively(root.left)
            right_height = self._heightRecursively(root.right)
            return max(left_height, right_height) + 1

    # Método para contar los nodos hoja
    def countLeaves(self):
        return self._countLeavesRecursively(self.root)

    def _countLeavesRecursively(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        return self._countLeavesRecursively(root.left) + self._countLeavesRecursively(root.right)


for _ in range(int(input())):
    num=map(int, input().split(' '))
    bst = BinarySearchTree()
    for i in num:
        if i==-1:break
        bst.insert(i)
    height=bst.height()
    leaves=bst.countLeaves()
    variable=2**(height-1)
    if variable==leaves:print('completo')
    else:print('no')