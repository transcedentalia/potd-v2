import random

__author__ = 'alina'


class Node():
    def __init__(self, info, next=None):
        self.info = info
        self.next = next


class LinkedList():
    def __init__(self):
        self.head = None

    def addNode(self, info):
        newNode = Node(info, None)
        newNode.next = self.head
        self.head = newNode

    def print(self):
        node = self.head
        while node:
            print(node.info, end=" ")
            node = node.next
        print("\n")

    def getNthElement(self, n):
        if n <= 0:
            return None

        i = 1
        node = self.head
        while node:
            if i == n:
                return node

            if not node.next:
                return None

            node = node.next
            i += 1
        return None

    def deleteNode(self, nodeInfoToDelete):
        if not nodeInfoToDelete:
            return

        if self.head.info == nodeInfoToDelete:
            self.head = self.head.next
            return

        node = self.head
        while node:
            if node.next:
                if node.next.info == nodeInfoToDelete:
                    node.next = node.next.next
            else:
                break
            node = node.next

    def getNthRearElement(self, n):
        if not self.head or n <= 0:
            return None

        node1 = node2 = self.head
        for i in range(n):
            if not node1:
                return
            node1 = node1.next

        while node1:
            node1 = node1.next
            node2 = node2.next

        return node2

    def getMiddleElement(self):
        if not self.head:
            return

        node1 = node2 = self.head
        while node1:
            if not node1.next:
                return node2

            node1 = node1.next.next
            node2 = node2.next

        return node2


    def reverseList(self):
        if not self.head:
            return

        prevNode = None
        currentNode = self.head
        nextNode = currentNode.next

        while nextNode:
            currentNode.next = prevNode
            prevNode = currentNode
            currentNode = nextNode
            nextNode = nextNode.next

        currentNode.next = prevNode
        self.head =currentNode

    def removeDuplicatesSortedList(self):
        if not self.head:
            return

        node = self.head

        while node:
            if node.next:
                if node.info == node.next.info:
                    node.next = node.next.next
                else:
                    node = node.next
            else:
                break

    def insertNodeInSortedList(self, info):
        newNode = Node(info)
        if not self.head:
            self.head = newNode
            return

        if newNode.info < self.head.info:
            newNode.next = self.head
            self.head = newNode
            return

        node = self.head
        while node:
            if node.next:
                if node.next.info > newNode.info:
                    newNode.next = node.next
                    node.next = newNode
                    break
                else:
                    node = node.next
            else:
                node.next = newNode
                break


def print_aux(node):
    while node:
        print(node.info, end=" ")
        node = node.next


def add_to_list_aux(l_head, l_rear, node):
    if not l_head:
        l_head = l_rear = node
    else:
        l_rear.next = node
        l_rear = node

    return l_head, l_rear


def merge_two_lists(l1, l2):
    if not l1 or not l2:
        return

    l3_head = l3_rear = None
    while l1 or l2:
        if l1 and l2:
            if l1.info < l2.info:
                l3_head, l3_rear = add_to_list_aux(l3_head, l3_rear, l1)
                l1 = l1.next
            else:
                l3_head, l3_rear = add_to_list_aux(l3_head, l3_rear, l2)
                l2 = l2.next
        else:
            if l1:
                l3_head, l3_rear = add_to_list_aux(l3_head, l3_rear, l1)
                l1 = l1.next
            else:
                l3_head, l3_rear = add_to_list_aux(l3_head, l3_rear, l2)
                l2 = l2.next
    l3_rear = None
    return l3_head


if __name__ == "__main__":
    myList = LinkedList()

    for i in range(20):
        myList.addNode(random.randint(1, 100))

    myList.print()
    print("The -3rd element is:", myList.getNthElement(-3))
    print("The 1st element is:", myList.getNthElement(1).info)
    print("The 5th element is:", myList.getNthElement(5).info)
    print("The 20th element is:", myList.getNthElement(20).info)
    print("The 23th element is:", myList.getNthElement(23))

    print("The 1st element rear:", myList.getNthRearElement(1).info)
    print("The 5th element rear:", myList.getNthRearElement(5).info)
    print("The 20th element rear:", myList.getNthRearElement(20).info)

    myList2 = LinkedList()
    myList2.addNode(2)
    myList2.addNode(5)
    myList2.addNode(3)
    myList2.addNode(9)
    myList2.addNode(7)

    myList2.print()
    print("Middle element:", myList2.getMiddleElement().info)
    myList2.deleteNode(7) # replace with a mid element, with the last one and with one that does not exist
    myList2.print()
    print("Middle element:", myList2.getMiddleElement().info)

    myList2.reverseList()
    myList2.print()

    myList3 = LinkedList()
    myList3.addNode(4)
    myList3.addNode(4)
    myList3.addNode(3)
    myList3.addNode(2)
    myList3.addNode(1)
    myList3.addNode(1)
    myList3.addNode(1)
    myList3.print()
    myList3.removeDuplicatesSortedList()
    myList3.print()
    myList3.insertNodeInSortedList(0)
    myList3.insertNodeInSortedList(3)
    myList3.insertNodeInSortedList(6)
    myList3.print()

    print("Merge two lists:")
    l1 = Node(1, Node(5, Node(7)))
    l2 = Node(2, Node(3, Node(4)))
    print_aux(merge_two_lists(l1, l2))


