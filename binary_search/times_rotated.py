def times_rotated(arr):
    start, end, length = 0, len(arr)-1, len(arr)
    while start <= end:
        mid = int(start + (end - start)/2)
        prev = int((mid + length - 1) % length)
        next = int((mid + 1) % length)
        if arr[prev] > arr[mid] < arr[next]:
            return f'Number of times rotated is {mid}'
        elif arr[mid] > arr[start]:
            start = mid + 1
        else:
            end = mid - 1
    return "Not rotated"

if __name__ == "__main__":
    a = [6, 7, 8, 9, 1, 2, 3, 4, 5]
    result = times_rotated(a)
    print(result)