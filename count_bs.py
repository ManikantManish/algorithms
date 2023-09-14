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
    return pos

def last_occurence(arr, ele):
    start, end, pos = 0, len(arr)-1, -1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == ele:
            pos = mid
            start = mid + 1
        elif arr[mid] < ele:
            start = mid + 1
        else:
            end = mid - 1
    return pos

if __name__ == "__main__":
    a = [1, 2, 3, 3, 4, 4, 4, 4, 5]
    ele = input("Enter a number: ")
    ele = int(ele)
    first_o = first_occurence(a, ele)
    if first_o == -1:
        print("Not found")
    else:
        last_o = last_occurence(a, ele)
        count = last_o - first_o + 1
        print(f"count of {ele} is {count}")
