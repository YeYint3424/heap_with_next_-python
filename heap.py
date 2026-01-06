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
        
def main():
    arr = [4, 10, 3, 5, 1, 2, 8, 7, 6, 9]

    print("Original array:", arr)

    heap_sort(arr)

    print("Sorted array:", arr)
    
main()

# add some comparison comments with other sorting algorithms
# Heap Sort has a time complexity of O(n log n) in the average and worst cases
        
