import timeit

#Create arrays here, contian random values from 0-10,000
def createArray(size, max):
  import random
  arr = [] #Declare array

  for i in range(size): #Loop thru until array size
    arr.append(random.randrange(0, max)) #Append random num to array
  return arr


#Sort thru array
def merge(one, two):
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
    
    lst_sizes = [n for n in range(150000, 250000, 10000)]
    
    for size in lst_sizes:
        
        arr = createArray(size, 10000)  # will create the array with size and each of the elements in 
                                        # the range 0 to 9999.
        # get the start time
        start_time = timeit.default_timer()    
        # call the merge sort
        arr = mergeSort(arr)
        # get the stop time
        stop_time = timeit.default_timer()
        # calculate the time taken
        time_taken = stop_time - start_time
        print("Array Size:", size, "time taken:", time_taken, "seconds")
    
    
if __name__ == "__main__":
    main()
