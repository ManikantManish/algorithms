def nearly_sorted(arr, ele):
    start, end = 0, len(arr)
    while start <= end:
        mid = int(start + (end - start)/2)
        if a[mid] == ele:
            return f'Found element at position {mid}'
        elif a[mid+1] == ele:
            return f'Found element at position {mid+1}'
        elif a[mid-1] == ele:
            return f'Found element at position {mid-1}'
        elif a[mid-1] < ele:
            start = mid + 2
        else:
            end = mid - 2
    return "Not found"

if __name__ == "__main__":
    a = [1, 3, 2, 4, 5, 7, 6, 8, 10, 9]
    ele = input("Enter a number")
    ele = int(ele)
    result = nearly_sorted(a, ele)
    print(result)