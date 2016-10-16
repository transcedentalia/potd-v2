from heapq import *
import heapq

__author__ = 'alina'


def merge_sort(arr):
    if len(arr) > 1:
        mid = (len(arr)) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


def quick_sort(arr, start, end):
    if start < end:
        pivot = partition(arr, start, end)
        quick_sort(arr, start, pivot - 1)
        quick_sort(arr, pivot + 1, end)


def partition(arr, start, end):
    pivot = arr[start]
    left = start + 1
    right = end

    done = False
    while not done:
        while left < right and arr[left] <= pivot:
            left += 1
        while arr[right] >= pivot and right >= left:
            right -= 1
        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[start], arr[right] = arr[right], arr[start]
    return right


def counting_sort(arr):
    counter = [0] * (len(arr) + 1)
    for elem in arr:
        counter[elem] += 1

    i = 0
    for j in range(len(counter)):
        while counter[j] > 0:
            arr[i] = j
            i += 1
            counter[j] -= 1


def kth_min_quick_sort(arr, k, start, end):
    if start == end:
        return arr[start]

    pivot = partition(arr, start, end)
    if k == pivot:
        return arr[pivot]

    if k < pivot:
        return kth_min_quick_sort(arr, k, start, pivot - 1)
    else:
        return kth_min_quick_sort(arr, k - pivot, pivot + 1, end)


def kth_min_heap(arr, k):
    heap = []
    for elem in arr:
        if len(heap) < k:
            heapq.heappush(heap, elem)
        else:
            if heap[0] > elem:
                heapreplace(heap, elem)

    return heappop(heap)


def binary_search(arr, item):
    start = 0
    end = len(arr) - 1
    found = False

    while start <= end and not found:
        mid = (start + end) // 2
        if arr[mid] == item:
            found = True
            break
        else:
            if item < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
    return found


if __name__ == '__main__':
    a1 = [2, 10, 7, 12, 3, 0, 17]
    merge_sort(a1)
    print("Merge sort:", a1)

    a2 = [13, 9, 4, 1, 20, 15, 3, 2]
    quick_sort(a2, 0, len(a2) - 1)
    print("Quick sort:", a2)

    a3 = [8, 3, 4, 1, 5, 7, 2, 6]
    counting_sort(a3)
    print("Counting sort:", a3)

    print("3rd smallest element(heap):", kth_min_heap(a2, 3))
    print("3rd smallest element(quick sort):", kth_min_quick_sort(a2, 3, 0, len(a2) - 1))

    a4 = [1,2,3,4,6,7,9]
    print(binary_search(a4, 7))