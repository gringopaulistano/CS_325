#Create arrays here, contain random values from 0-10,000
def createArray(size, max):
  import random
  arr = [] #Declare array

  for i in range(size): #Loop thru until array size
    arr.append(random.randrange(0,max)) #Append random num to array

  return arr

#Sort thru array
def merge(one,two):
  j = 0 #Left counter
  k = 0 #Right counter
  final = [] #array to hold sorted

  while(j < len(one) and k < len(two)):

    if(one[j] < two[k]):
      final.append(one[j])
      j += 1
    else:
      final.append(two[k])
      k += 1


  #copy additional elements into final array
  while j < len(one):
    final.append(one[j])
    j += 1

  while k < len(two):
    final.append(two[k])
    k += 1
    
  return final

#Recursive calls to sort array
def mergeSort(arr):

  if len(arr) == 0  or len(arr) == 1:
      return arr

  #Continue recursive calls
  mid = len(arr)//2
  left = mergeSort(arr[:mid])
  right = mergeSort(arr[mid:])
  return merge(left, right)


def main():
    inputFile = open("data.txt","r")
    outputFile = open("merge.txt","w")

    for line in inputFile:
        newArr = list(map(int,line.split())) #Move each int in lines to new array
        newArr2 = newArr[1:] #Skip first number in array 

        arrSorted = mergeSort(newArr2)

        for i in arrSorted:
            outputFile.write(str(i) + ' ')

        outputFile.write('\n')
        
    inputFile.close()
    outputFile.close()


if __name__ == "__main__":
    main()
