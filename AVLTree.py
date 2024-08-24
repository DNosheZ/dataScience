class Node(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree(object):
    def __init__(self):
        self.size = 0
        self.root = None

    def insert(self, key):
        if not self.search(key):
            self.root = self._insertRecursively(self.root, key)

    def _insertRecursively(self, root, key):
        if not root:
            new_node = Node(key)
            self.size += 1
            return new_node
        elif key < root.key:
            root.left = self._insertRecursively(root.left, key)
        else:
            root.right = self._insertRecursively(root.right, key)

        root.height = 1 + max(self._getNodeHeight(root.left),
                              self._getNodeHeight(root.right))

        balanceFactor = self._getNodeBalance(root)
        if balanceFactor > 1:
            if key < root.left.key:
                return self._rightRotate(root)
            else:
                root.left = self._leftRotate(root.left)
                return self._rightRotate(root)

        if balanceFactor < -1:
            if key > root.right.key:
                return self._leftRotate(root)
            else:
                root.right = self._rightRotate(root.right)
                return self._leftRotate(root)

        return root

    def delete(self, key):
        self.size -= self.search(key)
        self.root = self._deleteRecursively(self.root, key)

    def _deleteRecursively(self, root, key):

        if not root:
            return root
        elif key < root.key:
            root.left = self._deleteRecursively(root.left, key)
        elif key > root.key:
            root.right = self._deleteRecursively(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self._getMin(root.right)
            root.key = temp
            root.right = self._deleteRecursively(root.right, temp)
        if root is None:
            return root

        root.height = 1 + max(self._getNodeHeight(root.left), self._getNodeHeight(root.right))
        balanceFactor = self._getNodeBalance(root)

        if balanceFactor > 1:
            if self._getNodeBalance(root.left) >= 0:
                return self._rightRotate(root)
            else:
                root.left = self._leftRotate(root.left)
                return self._rightRotate(root)
        if balanceFactor < -1:
            if self._getNodeBalance(root.right) <= 0:
                return self._leftRotate(root)
            else:
                root.right = self._rightRotate(root.right)
                return self._leftRotate(root)
        return root

    def _leftRotate(self, z):
        y = z.right
        aux = y.left
        y.left = z
        z.right = aux
        z.height = 1 + max(self._getNodeHeight(z.left), self._getNodeHeight(z.right))
        y.height = 1 + max(self._getNodeHeight(y.left), self._getNodeHeight(y.right))
        return y

    def _rightRotate(self, z):
        y = z.left
        aux = y.right
        y.right = z
        z.left = aux
        z.height = 1 + max(self._getNodeHeight(z.left), self._getNodeHeight(z.right))
        y.height = 1 + max(self._getNodeHeight(y.left), self._getNodeHeight(y.right))
        return y

    def _getNodeHeight(self, root):
        if not root:
            return 0
        return root.height

    def _getNodeBalance(self, root):
        if not root:
            return 0
        return self._getNodeHeight(root.left) - self._getNodeHeight(root.right)

    def _getMin(self, root):
        if root is None:
            return None
        elif root.left is None:
            return root.key
        return self._getMin(root.left)

    def _getMax(self, root):
        if root is None:
            return None
        elif root.right is None:
            return root.key
        return self._getMin(root.right)
    
    def search(self, key):
        return self._searchRecursively(self.root, key) != None

    def _searchRecursively(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self._searchRecursively(root.left, key)
        else:
            return self._searchRecursively(root.right, key)

    def inOrder(self):
        elements = []
        self._inOrderRecursively(self.root, elements)
        return elements

    def _inOrderRecursively(self, root, elements):
        if root:
            self._inOrderRecursively(root.left, elements)
            elements.append(root.key)
            self._inOrderRecursively(root.right, elements)

    def PosOrder(self):
        elements = []
        self._inOrderRecursively(self.root, elements)
        return elements

    def _inOrderRecursively(self, root, elements):
        if root:
            self._inOrderRecursively(root.left, elements)
            self._inOrderRecursively(root.right, elements)
            elements.append(root.key)
            
    def popMin(self):
        if self.size == 0:
            return None
        else:
            key = self._getMin(self.root)
            self.delete(key)
            return key
        
    def popMax(self):
        if self.size == 0:
            return None
        else:
            key = self._getMax(self.root)
            self.delete(key)
            return key

    def getTreeHeight(self,root):
        if not root:return 0
        left_height=self.getTreeHeight(root.left)
        right_height=self.getTreeHeight(root.right)
        return 1+max(left_height,right_height) 
     
    def countDeepestLeaves(self):
        max_height = self.getTreeHeight(self.root)
        return self._countDeepestLeavesRecursively(self.root, 1, max_height)

    def _countDeepestLeavesRecursively(self, root, current_level, max_height):
        if not root:
            return 0
        if not root.left and not root.right and current_level == max_height:
            return 1
        return (self._countDeepestLeavesRecursively(root.left, current_level + 1, max_height) +
                self._countDeepestLeavesRecursively(root.right, current_level + 1, max_height))
    
    def childrenDescriptionPerLevel(self):
        if not self.root:
            return []

        from collections import deque

        result = []
        queue = deque([(self.root, 0)])

        while queue:
            node, level = queue.popleft()

            if len(result) == level:
                result.append("")

            if node.left and node.right:
                result[level] += ".2"
            elif node.left and not node.right:
                result[level] += ".-1"
            elif not node.left and node.right:
                result[level] += ".1"
            else:
                result[level] += ".0"

            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        return result

    def print_tree_rotated(self, node=None, level=0):
        if node is None:
            node = self.root
        if node.right:
            self.print_tree_rotated(node.right, level + 1)
        print('\t' * level + str(node.key))
        if node.left:
            self.print_tree_rotated(node.left, level + 1)

    def particles_colisionator(self):
        while self.root.left is not None and self.root.right is not None:
            max_molecule=self.popMax()
            min_molecule=self.popMin()
            if not self.search(max_molecule-min_molecule): self.insert(max_molecule-min_molecule)
        return self.root

        
# #Ejercicio 1
# for _ in range(int(input())):
#     cadena=map(str, input().split(' '))
#     arbol=AVLTree()
#     for c in cadena:
#         if c=='#':break
#         arbol.insert(c)
#     posOrderList="".join(map(str,arbol.PosOrder()))
#     print(posOrderList)

# #Ejercicio 2->genera errores para arboles totalmente descendentes o ascendentes
# for _ in range(int(input())):
#     cadena=map(int, input().split(' '))
#     arbol=AVLTree()
#     for c in cadena:
#         if c==-1:break
#         arbol.insert(c)
#     print(arbol.countDeepestLeaves())

# #Ejercicio 3-> cantar la cantidad de hijos que posee cada nivel
# while True:
#     bmax=int(input())
#     if bmax==0:break
#     cadena=map(int, input().split(' '))
#     arbol=AVLTree()
#     for c in cadena:
#         if c==-1:break
#         arbol.insert(c)
#     print('.'.join('.'.join(h[1:]) for h in [s.split(".") for s in arbol.childrenDescriptionPerLevel()]))

#Ejercicio 4
def FibonacciList(N):
    if N == 1:
        return 1
    elif N == 2:
        return 2
    else:
        a, b = 1, 2
        for _ in range(3, N + 1):
            a, b = b, a + b
        return b

for _ in range(int(input())):
    cadena=int(input())
    arbol=AVLTree()
    for i in range(1,cadena+1):
        arbol.insert(FibonacciList(i))
    arbol.print_tree_rotated()
    

#Ejercicio 5
for _ in range(int(input())):
    cadena=list(map(int,input().split(' ')))
    arbol=AVLTree()
    for i in cadena:
        if i==-1:break
        arbol.insert(i)
    while arbol.root.left is not None and arbol.root.right is not None:
        max_molecule=arbol.popMax()
        min_molecule=arbol.popMin()
        if not arbol.search(max_molecule-min_molecule): arbol.insert(max_molecule-min_molecule)

    