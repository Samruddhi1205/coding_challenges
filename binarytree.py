#Find the shortest distance between two nodes in a binary tree

class newNode:
 
  
    def __init__(self, data):
        self.key = data
        self.left = None
        self.right = None
 

def insert(root, key):
    if root == None:
        root = newNode(key)
    elif root.key > key:
        root.left = insert(root.left, key)
    elif root.key < key:
        root.right = insert(root.right, key)
    return root
 

def distanceFromRoot(root, x):
    if root.key == x:
        return 0
    elif root.key > x:
        return 1 + distanceFromRoot(root.left, x)
    return 1 + distanceFromRoot(root.right, x)
 

def distanceBetween2(root, a, b):
    if root == None:
        return 0
 
   
    if root.key > a and root.key > b:
        return distanceBetween2(root.left, a, b)
 
    
    if root.key < a and root.key < b: # same path
        return distanceBetween2(root.right, a, b)
 
    
    if root.key >= a and root.key <= b:
        return (distanceFromRoot(root, a) + distanceFromRoot(root, b))
 

def findDistWrapper(root, a, b):
    if a > b:
        a, b = b, a
    return distanceBetween2(root, a, b)
 

if __name__ == '__main__':
    root = None
    root = insert(root, 20)
    insert(root, 10)
    insert(root, 5)
    insert(root, 15)
    insert(root, 30)
    insert(root, 25)
    insert(root, 35)
    a, b = 5, 35
    print(findDistWrapper(root, 5, 35))
