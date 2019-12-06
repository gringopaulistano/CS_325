from timeit import default_timer as timer
import random

FILENAME = 'bin.txt'

def first_fit(weights, cap):
  start = timer()
  bins = [] #list to hold bins
  for w in weights: #iterate thru weights
    new_bin = True
    for i in range(len(bins)): #loop thru each bin
      b = bins[i]
      if b + w <= cap: #if space for item
        bins[i] = b + w #Add to bin
        new_bin = False
        break
    
    if new_bin:
      bins.append(w) #Open new bin

  end = timer()
  exec_time = round((end - start) * 1000000, 2)

  return len(bins), exec_time;


def best_fit(weights, cap):
  start = timer()
  bins = []
  for w in weights:
    best_so_far = -1
    min_gap = 10000000
    for i in range(len(bins)): #Loop thru bins
      b = bins[i]
      if b + w <= cap and cap - (b+w) < min_gap:
        best_so_far = i #set to current best fit
        min_gap = cap - (b+w) #set to space left

    if best_so_far != -1:
      bins[best_so_far] += w #Add item to correct bin
    else:
      bins.append(w) #Else, open new bin

  end = timer()
  exec_time = round((end - start) * 1000000,2)
  return len(bins), exec_time


def first_fit_decreasing(weights, cap):
  start = timer()
  weights_sorted = weights.copy()
  merge(weights_sorted)
  bins = [] #list of bins
  for w in weights_sorted: #iterate thru sorted weights
    new_bin = True
    for i in range(len(bins)):
      b = bins[i]
      if b + w <= cap:
        bins[i] = b + w
        new_bin = False
        break

    if new_bin:
      bins.append(w)

  end = timer()
  exec_time = round((end - start) * 1000000, 2)
  return len(bins), exec_time



def merge(list): #merge sort implementation
  if len(list) > 1:
    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]

    merge(left)
    merge(right)

    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
      if left[i] > right[j]:
        list[k] = left[i]
        i += 1
      else:
        list[k] = right[j]
        j += 1
      k += 1

    while i < len(left):
      list[k] = left[i]
      k += 1
      i += 1

    while j < len(right):
      list[k] = right[j]
      k += 1
      j += 1
  return list



def read_file():
  filepath = "bin.txt"
  with open(filepath) as fp:
    lines = fp.readlines() #Read in file

  lines = [line.strip() for line in lines] #Remove whitespaces
  test_list = []
  test_cases = int(lines[0]) #Read in first line, # of test cases
  line_num = 1
  for test in range(test_cases): #Loop thru test cases, fill in data
    cap = int(lines[line_num])
    line_num += 1
    num_packs = int(lines[line_num])
    line_num += 1;
    weights = lines[line_num].split()
    weights = [int(w) for w in weights] #Weight is an INT not STR
    test_list.append([cap, num_packs, weights]) #Add test case data to list
    line_num += 1
    #print(cap)

  return test_list

def random_cases():
  test_list = []
  test_cases = 20 #Random cases
  line_num = 1
  for test in range(test_cases): #Loop thru each test case, generate random nums
    cap = random.randint(10,20)
    num_packs = random.randint(20,30)
    weights = [random.randint(0, cap) for _ in range(num_packs)]
    test_list.append([cap, num_packs, weights]) #Add test case to list

  return test_list


def test_file_cases():
    """
    Perform testing on cases from file.

    """
    test_list = read_file()
    print("*****Testing file cases*****")
    print("*Execution time is in micro seconds*")
    print('')
    for i in range(len(test_list)): #iterate thru list of cases
        #print(test_list[i])
        test = test_list[i] #Set test to current case
        ff_result, ff_time = first_fit(test[2], test[0])
        ffd_result, ffd_time = first_fit_decreasing(test[2], test[0])
        bf_result, bf_time = best_fit(test[2], test[0])
        print("Test Case %s \nFirst Fit: %s, Time: %s \n"
              "First Fit Decreasing: %s, Time: %s \n" 
              "Best Fit: %s, Time : %s \n" %
              ((i+1), ff_result, ff_time,
              ffd_result, ffd_time,
              bf_result, bf_time))
        #print(test[0])


def test_rand_cases():
  test_list = random_cases()
  print("\n\n*****Testing Random Cases*****\n")
  print("*Execution time in micro seconds*\n")


  for i in range(len(test_list)): #Iterate thru list with random cases
    print("Testcase %s: %s - \n" % ((i+1), test_list[i]), file=open("data.txt", "a"))
    test = test_list[i]
    ff_result, ff_time = first_fit(test[2], test[0])
    ffd_result, ffd_time = first_fit_decreasing(test[2], test[0])
    bf_result, bf_time = best_fit(test[2], test[0])

    print("First Fit: %s - Time: %s - \n"
          "First Fit Decreasing: %s - Time: %s - \n" 
          "Best Fit: %s - Time: %s - \n" %
          (ff_result, ff_time,
          ffd_result, ffd_time,
          bf_result, bf_time), file=open("data.txt", "a"))
    print("\n")

    for i in range(len(test_list)): #Iterate thru list with random cases
      print("Testcase %s: %s - \n" % ((i+1), test_list[i]))
      test = test_list[i]
      ff_result, ff_time = first_fit(test[2], test[0])
      ffd_result, ffd_time = first_fit_decreasing(test[2], test[0])
      bf_result, bf_time = best_fit(test[2], test[0])

      print("First Fit: %s - Time: %s - \n"
      "First Fit Decreasing: %s - Time: %s - \n" 
      "Best Fit: %s - Time: %s - \n" %
      (ff_result, ff_time,
      ffd_result, ffd_time,
      bf_result, bf_time))
    #print("\n")



def main():

  test_file_cases()

  test_rand_cases()


main()



