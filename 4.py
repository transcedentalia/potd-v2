from heapq import *
import sys

__author__ = 'alina'


def extract_min(array):
    min = array[0]
    array[0] = array[-1]
    array.pop()

    heapify(array, 0)

    return min


def get_parent(i):
    return (i - 1) // 2


def insert_key(array, key_value):
    array.append(key_value)
    i = len(array) - 1
    parent = get_parent(i)

    while i > 0 and array[parent] > array[i]:
        array[parent], array[i] = array[i], array[parent]
        i = parent


def get_left_child(i):
    return 2 * i + 1


def get_right_child(i):
    return 2 * i + 2


def heapify(array, i):
    smallest = i
    left_child = get_left_child(i)
    right_child = get_right_child(i)

    if left_child < len(array) and array[left_child] < array[smallest]:
        smallest = left_child

    if right_child < len(array) and array[right_child] < array[smallest]:
        smallest = right_child

    if smallest != i:
        array[smallest], array[i] = array[i], array[smallest]
        heapify(array, smallest)


def decrease_key(array, i, new_val):
    if i < 0 or i >= len(array):
        return

    array[i] = new_val
    parent = get_parent(i)

    while i > 0 and array[parent] > array[i]:
        array[parent], array[i] = array[i], array[parent]
        i = parent


def delete_key(array, i):
    decrease_key(array, i, -sys.maxsize)
    extract_min(array)


class Node:
    def __init__(self, info, next=None):
        self.info = info
        self.next = next

    def __lt__(self, other):
        if self.info < other.info:
            return True
        else:
            return False

def print_list_aux(node):
    while node:
        print(node.info, end=" ")
        node = node.next

def merge_k_lists(lists):
    heap = []
    result_head = result_rear = None
    for i, l in enumerate(lists):
        heappush(heap, l)

    while heap:
        min_node = heappop(heap)
        if not result_head:
            result_head = result_rear = min_node
        else:
            result_rear.next = min_node
            result_rear = result_rear.next

        if min_node.next:
            heappush(heap, min_node.next)

    return result_head


def get_kth_min_from_sorted_matrix(matrix, k):
    heap = []
    for i, elem in enumerate(matrix[0]):
        heappush(heap, (elem, 0, i))

    temp = sys.maxsize
    while k > 0:
        temp, i, j = heappop(heap)
        heappush(heap, (matrix[i + 1][j], i + 1, j))

        k -= 1

    return temp


def heapify2(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        heapify2(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    for i in range(n - 1, -1, -1):
        heapify2(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify2(arr, i, 0)

if __name__ == "__main__":
    heap = []
    insert_key(heap, 4)
    insert_key(heap, 2)

    print(extract_min(heap))

    insert_key(heap, 6)

    print(extract_min(heap))

    insert_key(heap, 7)
    insert_key(heap, 8)

    print(heap)
    delete_key(heap, 1)
    print(heap)

    print("\nMerge k lists:")
    l1 = Node(1, Node(6, Node(7)))
    l2 = Node(2, Node(4, Node(5)))
    l3 = Node(3, Node(8, Node(10)))

    res = merge_k_lists([l1, l2, l3])
    print_list_aux(res)

    matrix = [[10, 20, 30, 40], [15, 25, 35, 45], [24, 29, 37, 48], [32, 33, 39, 50]]
    print("\n7th smallest element from matrix:", get_kth_min_from_sorted_matrix(matrix, 7))

    print("\nHeap sort:")
    arr = [12, 11, 13, 5, 6, 7]
    heap_sort(arr)
    for elem in arr:
        print(elem, end=" ")
