def reverseList(arr, n, m):
    if n < 0 or m >= len(arr) or n >= m:
        return arr

    subarray = arr[n:m+1]

    subarray.reverse() 

    arr[n:m+1] = subarray

    return arr