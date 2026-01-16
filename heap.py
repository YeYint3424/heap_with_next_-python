import time
import random
import sys
sys.setrecursionlimit(10**7)

# ---------------- HEAP SORT ----------------
def heapify(arr, n, i):
    largest = i        # Assume root is largest
    left = 2 * i + 1   # Left child
    right = 2 * i + 2  # Right child

    # Check left child
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check right child
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Swap and continue heapifying if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Build Max Heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

# ---------------- BUBBLE SORT ----------------
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# ---------------- SELECTION SORT ----------------
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# ---------------- INSERTION SORT ----------------
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# ---------------- MERGE SORT ----------------
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# ---------------- QUICK SORT ----------------
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# ---------------- TIME MEASUREMENT ----------------
def measure_time(sort_func, arr, returns_new=False):
    start = time.perf_counter()
    if returns_new:
        sort_func(arr)
    else:
        sort_func(arr)
    end = time.perf_counter()
    return end - start

def main():
    sizes = [50, 100, 1000]

    tests = [
        ("Bubble Sort", bubble_sort, False),
        ("Selection Sort", selection_sort, False),
        ("Insertion Sort", insertion_sort, False),
        ("Merge Sort", merge_sort, False),
        ("Heap Sort", heap_sort, False),
        ("Quick Sort", quick_sort, True)
    ]

    for SIZE in sizes:
        original = [random.randint(1, 10000) for _ in range(SIZE)]

        print(f"\nRuntime Comparison (n = {SIZE})\n")

        for name, func, returns_new in tests:
            arr_copy = original.copy()
            t = measure_time(func, arr_copy, returns_new)
            print(f"{name:<15}: {t:.6f} seconds")

main()
