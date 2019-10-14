import timeit


# Create arrays here, contian random values from 0-10,000
def createArray(size, max):
    import random
    arr = []  # Declare array

    for i in range(size):  # Loop thru until array size
        arr.append(random.randrange(0, max))  # Append random num to array
    return arr


def stoogeSort(arr, l, r):
    if (l >= r):
        return

    if (arr[l] > arr[r]):
        temp = arr[l]
        arr[l] = arr[r]
        arr[r] = temp

    # print("Value: ", arr[i])
    # print(arr[j])
    # i == l

    if (r - l + 1) >= 3:
        stooger = ((r - l + 1) // 3)
        stoogeSort(arr, l, (r - stooger))  # Initial
        stoogeSort(arr, l + stooger, (r))  # Last
        stoogeSort(arr, l, (r - stooger))  # Initial
    return arr


def main():
    lst_sizes = [n for n in range(100, 1000, 100)]

    for size in lst_sizes:
        arr = createArray(size, 1000)
        start_time = timeit.default_timer()
        last = len(arr) - 1
        arr = stoogeSort(arr, 0, last)
        stop_time = timeit.default_timer()
        time_taken = stop_time - start_time
        print("Array Size:", size, "time taken:", time_taken, "seconds")


if __name__ == "__main__":
    main()

