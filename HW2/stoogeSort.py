def stoogeSort(arr, l, r):
    if(l>=r):
        return

    if(arr[l] > arr[r]):
        temp = arr[l]
        arr[l] = arr[r]
        arr[r] = temp

    #print("Value: ", arr[i])
    #print(arr[j])
    #i == l

    if (r-l+1) >= 3:
        stooger = ((r-l+1)//3)
        stoogeSort(arr, l, (r-stooger)) #Initial
        stoogeSort(arr, l + stooger, (r)) #Last
        stoogeSort(arr, l, (r-stooger)) #Initial
    return arr

def main():
        inputFile = open("data.txt","r")
        outputFile = open("stooge.txt","w")

        for line in inputFile:
            newArr = list(map(int,line.split())) #Move each int in lines to new array
            newArr2 = newArr[1:] #Skip first number in array

            last = len(newArr2) - 1
            sortedArr = stoogeSort(newArr2, 0, last)

            for i in sortedArr:
                outputFile.write(str(i) + ' - ')

            outputFile.write('\n')

        inputFile.close()
        outputFile.close()

if __name__ == "__main__":
    main()
