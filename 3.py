__author__ = 'alina'

import sys
from collections import deque

class TreeNode:
    def __init__(self, info, left=None, right=None):
        self.info = info
        self.left = left
        self.right = right


class MultiWayTreeNode:
    def __init__(self, info, childrenList=None):
        self.info = info
        if childrenList == None:
            self.childrenList = []
        else:
            self.childrenList = childrenList

class MultiWayTreeNode2:
    def __init__(self, info, child=None, brother=None):
        self.info = info
        self.child = child
        self.brother = brother


def preorderMultiWay2(root):
    if not root:
        return

    print(root.info, end=" ")
    preorderMultiWay2(root.child)
    preorderMultiWay2(root.brother)

def postorderMultiWay2(root):
    if not root:
        return

    node = root
    while node != None:
        postorderMultiWay2(node.child)
        print(node.info, end=" ")
        node = node.brother


def preorderMultiWay(root):
    if not root:
        return

    print(root.info, end=" ")
    for childNode in root.childrenList:
        preorderMultiWay(childNode)


def countNodesRec(root):
    if not root:
        return 0

    return 1 + countNodesRec(root.left) + countNodesRec(root.right)


def countLeaves(root):
    if not root:
        return 0

    if not root.left and not root.right:
        return 1

    return countLeaves(root.left) + countLeaves(root.right)


def getHeight(root):
    if not root:
        return 0

    return 1 + max(getHeight(root.left), getHeight(root.right))

def getHeightIter(root):
    if not root:
        return

    currentHeight = maxHeight = 1

    stack = deque([(root, currentHeight)])
    while stack:
        node, currentHeight = stack.pop()
        if currentHeight > maxHeight:
            maxHeight = currentHeight

        if node.right:
            stack.append((node.right, currentHeight + 1))
        if node.left:
            stack.append((node.left, currentHeight + 1))

    return maxHeight


def inorderRec(root):
    if not root:
        return

    inorderRec(root.left)
    print(root.info, end=" ")
    inorderRec(root.right)


def inorderIter(root):
    crtNode = root
    stack = deque()

    while stack or crtNode:
        if not crtNode:
            crtNode = stack.pop()

            print(crtNode.info, end=" ")
            crtNode = crtNode.right
        else:
            stack.append(crtNode)
            crtNode = crtNode.left

def preorderRec(root):
    if not root:
        return

    print(root.info, end=" ")
    preorderRec(root.left)
    preorderRec(root.right)


def preorderIter(root):
    if not root:
        return

    stack = deque([root])
    while stack:
        node = stack.pop()
        print(node.info, end=" ")

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)


def postorderRec(root):
    if not root:
        return

    postorderRec(root.left)
    postorderRec(root.right)
    print(root.info, end=" ")


def postorderIter(root):
    stack1 = deque([root])
    stack2 = deque()
    while stack1:
        node = stack1.pop()
        stack2.append(node)
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)

    while stack2:
        print(stack2.pop().info, end=" ")


def getMinNodeBST(root):
    while root.left:
        root = root.left
    return root.info


def preorderGenerator(root):
    if not root:
        raise StopIteration

    yield root.info

    yield from preorderGenerator(root.left)
    yield from preorderGenerator(root.right)


def preorderListAux(root, result):
    if not root:
        return

    result.append(root.info)
    preorderListAux(root.left, result)
    preorderListAux(root.right, result)


def preorderList(root):
    result = []
    preorderListAux(root, result)

    return result


def checkSubtree(root1, root2):
    if not root1 and not root2:
        return True

    if not root1 or not root2:
        return False

    if root1.info == root2.info:
        foundRoot = checkSubtree(root1.left, root2.left) and checkSubtree(root1.right, root2.right)
        if foundRoot:
            return True

    foundLeft = checkSubtree(root1.left, root2)
    if foundLeft:
        return True
    return checkSubtree(root1.right, root2)


def isBst(root, inf=-sys.maxsize, sup=sys.maxsize):
    if not root:
        return True

    if not (inf < root.info < sup):  # if root.info <= inf or root.info >= sup
        return False

    return isBst(root.left, inf, root.info) and isBst(root.right, root.info, sup)

def inorderAux(root):
    if not root:
        raise StopIteration

    yield from inorderAux(root.left)
    yield root.info
    yield from inorderAux(root.right)


def isBST2(root):
    inorderTraversal = inorderAux(root)
    prevNode = next(inorderTraversal)
    for node in inorderTraversal:
        if prevNode > node:
            return False
        prevNode = node
    return True


def levelOrderTraversal(root):
    queue = deque([(root, 1)])
    crtLevel = 1
    while queue:
        crtNode, level = queue.popleft()
        if crtLevel < level:
            print("\n")
            crtLevel = level
        print(crtNode.info, end=" ")
        if crtNode.left:
            queue.append((crtNode.left, level + 1))
        if crtNode.right:
            queue.append((crtNode.right, level + 1))


def deleteBST(root):
    if not root:
        return

    deleteBST(root.left)
    deleteBST(root.right)

    root.left = None
    root.right = None


def printRootToLeavesPaths(root, path):
    if not root:
        return

    path.append(root)
    if not root.left and not root.right:
        for node in path:
            print(node.info, end=" ")
        print("\n")
        path.pop()
        return

    printRootToLeavesPaths(root.left, path)
    printRootToLeavesPaths(root.right, path)
    path.pop()


def levelOrderSpiralTraversal(root):
    if not root:
        return

    queue = deque([(root, 1)])
    currentLevel = 1
    leftToRight = True
    while queue:
        node = None
        level = 0
        if leftToRight:
            node, level = queue.popleft()
        else:
            node, level = queue.pop()

        if level > currentLevel:
            currentLevel = level
            print("\n")

            if leftToRight:
                queue.appendleft((node, level))
            else:
                queue.append((node,level))

            leftToRight = not leftToRight

            if leftToRight:
                node, level = queue.popleft()
            else:
                node, level = queue.pop()

        print(node.info, end=" ")

        if leftToRight:
            if node.left:
                queue.append((node.left, currentLevel + 1))
            if node.right:
                queue.append((node.right, currentLevel + 1))
        else:
            if node.right:
                queue.appendleft((node.right, currentLevel + 1))
            if node.left:
                queue.appendleft((node.left, currentLevel + 1))


def levelOrderSpiralTraversal2(root):
    if not root:
        return

    queue = deque([(root, 1)])
    currentLevel = 1
    while queue:
        node, level = queue.popleft()
        if level > currentLevel:
            queue.appendleft((node, level))
            queue = queue.reverse()
            print("\n")
            node, level = queue.popleft
        print(node.info, end=" ")
        if node.left:
            queue.append((node.left, level))
        if node.right:
            queue.append((node.right, level))


def lcaBST(root, val1, val2):
    if not root:
        return None

    stack = deque([root])
    while stack:
        node = stack.pop()
        if val1 < node.info < val2:
            return node
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)


def lca(root, val1, val2):
    if not root:
        return None

    if val1 == root.info or val2 == root.info:
        return root

    lcal = lca(root.left, val1, val2)
    lcar = lca(root.right, val1, val2)

    if lcal and lcar:
        return root

    if lcar:
        return lcar

    return lcal


def diameter(root):
    if not root:
        return 0, 0

    dl, hl = diameter(root.left)
    dr, hr = diameter(root.right)

    d = max(dl, dr, hl + hr + 1)
    h = 1 + max(hl, hr)

    return d, h


def isBalanced(root):
    if not root:
        return False, 0, 0

    if not root.left and not root.right:
        return True, 1, 1

    if not root.left or not root.right:
        return True, 1, 1

    isBalancedLeft, maxDepthLeft, minDepthLeft = isBalanced(root.left)
    isBalancedRight, maxDepthRight, minDepthRight = isBalanced(root.right)

    maxDepth = 1 + max(maxDepthLeft, maxDepthRight)
    minDepth = min(minDepthLeft, minDepthRight)

    if maxDepth - minDepth <= 1 and isBalancedLeft and isBalancedRight:
        return True, maxDepth, minDepth
    else:
        return False, maxDepth, minDepth


def checkChildrenSums(root):
    stack = deque([root])
    while stack:
        node = stack.pop()
        childrenSum = 0
        if node.left:
            childrenSum += node.left.info
        if node.right:
            childrenSum += node.right.info

        if sum != node.info:
            return False

        if node.right:
            stack.push(node.right)
        if node.left:
            stack.push(node.left)

    return True


def nodesKDistanceFromRoot(root, level, k):
    if not root:
        return

    if level == k:
        print(root.info, end=" ")
    nodesKDistanceFromRoot(root.left, level + 1, k)
    nodesKDistanceFromRoot(root.right, level + 1, k)


def getNodeAncestors(root, nodeVal, ancestors):
    if not root:
        return False

    if root.info == nodeVal:
        return True

    fouldLeft = getNodeAncestors(root.left, nodeVal, ancestors)
    foundRight = getNodeAncestors(root.right, nodeVal, ancestors)

    if fouldLeft or foundRight:
        ancestors.append(root)
        return True

    return False


def getNodeSuccessors(root, nodeVal, successors, found):
    if not root:
        return

    #print(root.info, nodeVal, successors, found, "\n")

    if root.info == nodeVal:
        found = True

    if found and root.info != nodeVal:
        successors.append(root)

    getNodeSuccessors(root.left, nodeVal, successors, found)
    getNodeSuccessors(root.right, nodeVal, successors, found)


def printBSTNodesInIntervalOrdered(root, k1, k2):
    if not root:
        return

    printBSTNodesInIntervalOrdered(root.left, k1, k2)
    if k1 <= root.info <= k2:
        print(root.info, end=" ")
    printBSTNodesInIntervalOrdered(root.right, k1, k2)


def inorderBSTAux(node):
    if not node:
        raise StopIteration

    yield from inorderAux(node.left)
    yield node.info
    yield from inorderAux(node.right)


def kSmallesteNodeInBST(node, k):
    inorderGenerator = inorderAux(node)
    for i in range(k - 1):
        next(inorderGenerator)

    print(next(inorderGenerator))


def levelOfKey(root, nodeVal):
    stack = deque([(root, 1)])
    while stack:
        node, level = stack.pop()
        if node.info == nodeVal:
            return level

        if node.right:
            stack.append((node.right, level + 1))

        if node.left:
            stack.append((node.left, level + 1))

    return -1


def getMaxWidth(root):
    queue = deque([(root, 1)])
    currentLevel = 1
    maxWidth = 1
    currentWidth = 0

    while queue:
        node, level = queue.popleft()
        if level == currentLevel:
            currentWidth += 1
        else:
            if currentWidth > maxWidth:
                maxWidth = currentWidth
            currentWidth = 1
            currentLevel = level

        if node.left:
            queue.append((node.left, currentLevel + 1))
        if node.right:
            queue.append((node.right, currentLevel + 1))

    return maxWidth


def addNodeToWidthArray(arrayNodes, node, width):
    if abs(width) < len(arrayNodes):
        tmp = arrayNodes[abs(width)]
        node.left = tmp.left
        node.right = None
        tmp.right = node
        arrayNodes[abs(width)] = node
    else:
        arrayNodes.append(node)
        node.right = None
        node.left = node


def levelOrder(root):
    queue = deque([(root, 0)])

    leftNodes = []
    rightNodes = []
    while queue:
        node, width = queue.popleft()
        if node.left:
            queue.append((node.left, width - 1))

        if node.right:
            queue.append((node.right, width + 1))

        print("#", node.info, width)
        if width >= 0:
            addNodeToWidthArray(rightNodes, node, width)
            if width == 0:
                addNodeToWidthArray(leftNodes, node, width)
        else:
            addNodeToWidthArray(leftNodes, node, width)

    return leftNodes, rightNodes


def printNodesAux(node):
    node = node.left
    while node:
        print(node.info, end=" ")
        node = node.right
    print("$", end=" ")


def printVerticalOrder(root):
    leftNodes, rightNodes = levelOrder(root)
    for i in range(len(leftNodes) - 1, 0, -1):
        printNodesAux(leftNodes[i])

    for node in rightNodes:
        printNodesAux(node)

if __name__ == "__main__":
    myTree = TreeNode(1, TreeNode(2, TreeNode(5), TreeNode(6)), TreeNode(3, None, TreeNode(4, TreeNode(7), None)))
    print("Number of nodes:", countNodesRec(myTree))
    print("Number of leaves:", countLeaves(myTree))
    print("Tree height rec:", getHeight(myTree))
    print("Tree height iter:", getHeightIter(myTree))

    print("Inorder rec:", end="")
    print(inorderRec(myTree))
    print("Inorder iter:", end="")
    print(inorderIter(myTree))

    print("Preorder rec:", end="")
    print(preorderRec(myTree))
    print("Preorder iter:", end="")
    print(preorderIter(myTree))

    print("Postorder rec:", end="")
    print(postorderRec(myTree))
    print("Postorder iter:", end="")
    postorderIter(myTree)

    print("\nisBST:", isBst(myTree))
    print("isBST2:", isBST2(myTree))

    print("Level order traversal:")
    print(levelOrderTraversal(myTree))

    print("Preorder:", preorderList(myTree))
    print("Preorder with generator:", list(preorderGenerator(myTree)))

    print("Root to leaves paths:")
    printRootToLeavesPaths(myTree, [])

    print("Spiral level traversal:")
    levelOrderSpiralTraversal(myTree)

    print("\nSpiral level traversal2:")
    levelOrderSpiralTraversal(myTree)

    print("\nLCA for 5 and 6 is ", lca(myTree, 5, 6).info)

    print("\nDiameter:", diameter(myTree))

    print("\nIs balanced:", isBalanced(myTree))

    print("\nCheckChildrenSum:", checkChildrenSums(myTree))

    print("\nNodes 3 dinstance away from root:")
    print(nodesKDistanceFromRoot(myTree, 1, 3))

    print("\nGet ancestors for 7:")
    ancestors = []
    getNodeAncestors(myTree, 7, ancestors)
    for ancestor in ancestors:
        print(ancestor.info, end=" ")

    print("\nGet successors for 1:")
    successors = []
    getNodeSuccessors(myTree, 1, successors, False)
    for successor in successors:
        print(successor.info, end=" ")

    myTree2 = TreeNode(7, TreeNode(5, TreeNode(2, None, TreeNode(3)), TreeNode(6)), TreeNode(10, TreeNode(8), None))
    print("\nLCA BST for 3 and 6 is", lcaBST(myTree2, 3, 6).info)

    print("\nBST Nodes between k1 and k2 in ascending order:")
    printBSTNodesInIntervalOrdered(myTree2, 6, 10)

    print("\n3rd smallest node in BST:", end="")
    kSmallesteNodeInBST(myTree2, 3)

    print("\nLevel of node 6:", levelOfKey(myTree2, 6))

    print("\nMax width:", getMaxWidth(myTree2))

    myMultiWayTree = MultiWayTreeNode(10, [MultiWayTreeNode(4), MultiWayTreeNode(8, [MultiWayTreeNode(2)]), MultiWayTreeNode(5, [MultiWayTreeNode(3), MultiWayTreeNode(11), MultiWayTreeNode(6)])])
    print("\nPreorder multi way tree(sons): ")
    preorderMultiWay(myMultiWayTree)

    myMultiWayTree2 = MultiWayTreeNode2(10, MultiWayTreeNode2(4, None, MultiWayTreeNode2(8, MultiWayTreeNode2(2), MultiWayTreeNode2(5, MultiWayTreeNode2(3, None, MultiWayTreeNode2(11, None, MultiWayTreeNode2(6)))))))
    print("\nPreorder multi way tree(son - brother): ")
    preorderMultiWay2(myMultiWayTree2)
    print("\nPostorder multi way tree(son - brother): ")
    postorderMultiWay2(myMultiWayTree2)

    print("\nPrint vertical order:")
    printVerticalOrder(myTree2)