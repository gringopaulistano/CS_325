import timeit

#Create arrays here, contian random values from 0-10,000
def createArray(size, max):
  import random
  arr = [] #Declare array

  for i in range(size): #Loop thru until array size
    arr.append(random.randrange(0,max)) #Append random num to array
  return arr


def insertSort(arr):

  for i in range(1, len(arr)): #Loop thru array
    cur = arr[i] #cur contains value of current position in array
    pos = i - 1 #starts at 1, contains pos of array

    while (pos >= 0) and (arr[pos] > cur): #If value on left larger
      arr[pos+1] = arr[pos] #Move to right
      pos -= 1

    arr[pos+1] = cur

def main():
    lst_sizes = [n for n in range(100,900,100)] 
    
    # executing a for loop for each of the element in the lst_size
    for size in lst_sizes:
        
        arr = createArray(size, 10000)  # will create the array with size and each of the elements in 
                                        # the range 0 to 9999.
        # get the start time
        start_time = timeit.default_timer()    
        # call the insertion sort
        insertSort(arr)
        # get the stop time
        stop_time = timeit.default_timer()
        # calculate the time taken
        time_taken = stop_time - start_time
        print("Array Size:", size, "time taken:", time_taken, "seconds") 
    

if __name__ == "__main__":
    main()
