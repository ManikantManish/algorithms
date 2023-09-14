def binary_search(arr, ele):
    start, end = 0, len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == ele:
            return f"At position {mid}"
        elif arr[mid] < ele:
            start = mid + 1
        else:
            end = mid - 1

    return "Not found"

if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ele = input("Enter number: ")
    ele = int(ele)
    result = binary_search(a, ele)
    print(result)
