def binary_search(arr, d):
    n = len(arr) - 1

    low = 0
    high = n

    while low <= high:
        mid = int(low + (high - low) / 2)

        if arr[mid] == d:
            return mid
        elif arr[mid] < d:
            low = mid + 1
        elif arr[mid] > d:
            high = mid - 1



if __name__ == "__main__":
    arr = [1,8,6,2,5,4,8,3,7]
    s = sorted(arr)

    print(s)

    print(binary_search(s, 7))
