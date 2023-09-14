def first_occurence(arr, ele):
    start, end, pos = 0, len(arr)-1, -1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == ele:
            pos = mid
            end = mid - 1
        elif arr[mid] < ele:
            start = mid + 1
        else:
            end = mid - 1
    if pos == -1:
        return "Not found"
    return f"First occurance of {ele} is at position {pos}"


if __name__ == "__main__":
    a = [1, 2, 3, 3, 4, 4, 4, 4, 5]
    ele = input("Enter a number: ")
    ele = int(ele)
    result = first_occurence(a, ele)
    print(result)