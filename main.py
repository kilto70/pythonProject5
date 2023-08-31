def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return low


def insert_position(arr, target):
    index = binary_search(arr, target)
    if index < len(arr) and arr[index] == target:
        return index
    elif index == 0:
        return 0
    elif index == len(arr):
        return len(arr)
    else:
        return index if target - arr[index - 1] <= arr[index] - target else index - 1


numbers = list(map(int, input("Enter a sequence of numbers separated by spaces: ").split()))
numbers.sort()
target = int(input("Enter a number to find its insert position: "))
result = insert_position(numbers, target)
print(f"The insert position for {target} is {result}")
