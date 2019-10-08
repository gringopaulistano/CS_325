def insertSort(arr):

  for i in range(1, len(arr)): #Loop thru array
    cur = arr[i] #cur contains value of current position in array
    pos = i - 1 #starts at 1, contains pos of array

    while (pos >= 0) and (arr[pos] > cur): #If value on left larger
      arr[pos+1] = arr[pos] #Move to right
      pos -= 1
    arr[pos+1] = cur

  return arr

def main():
  inputFile = open("data.txt","r")
  outputFile = open("insert.txt","w")

  for line in inputFile:
    newArr = list(map(int,line.split())) #Move each int in lines to new array
    newArr2 = newArr[1:] #Skip first number in array 

    sortedArr = insertSort(newArr2)
  
    for i in sortedArr:
      outputFile.write(str(i) + ' - ')

    outputFile.write('\n')
        
  inputFile.close()
  outputFile.close()

if __name__ == "__main__":
    main() 
