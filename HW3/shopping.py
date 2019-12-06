def knapsack(wt_lim,pr_wt_list):
  if len(pr_wt_list)==1:
    if pr_wt_list[0][1]>wt_lim:
      return []  #return empty list if weight > limit
    else: #Else return price of the only item
      return [pr_wt_list[0][0]]
    
  else: #More than 1 item in the list
    if pr_wt_list[-1][1]>wt_lim: #Last item > weight limit, remove and run knapsack
      return knapsack(wt_lim,pr_wt_list[:-1])
    else: 
      case1= knapsack(wt_lim-pr_wt_list[-1][1],pr_wt_list[:-1]) + [pr_wt_list[-1][0]]
      case2=knapsack(wt_lim,pr_wt_list[:-1])
      if sum(case1)>sum(case2): #Return larger sum of 2 cases, with and without item
        return case1
      else:
        return case2 

def main():
  outputFile = open("results.txt","w")
    
  with open("shopping.txt", "r+") as fo:

    t=int(fo.readline()) #Number of test cases
        
    for test_case in range(t):
      n=int(fo.readline()) #Number of items
      price_weight_list=[] #Empty list to store price, weight pairs of 'n' items
      
      for item in range(n):
        inp=map(int,fo.readline().split()) #Change to correct type
        inp_list=list(inp) #create list
        price_weight_list.append(inp_list) #Append pairs to list
                
      f=int(fo.readline()) #Number of family members
      f_list=[] #Empty list to store max weight for each family member
      for fam in range(f): #weight limits, correct type
        inp=int(fo.readline())
        f_list.append(inp)
            
      opt_dict={}  #Dictionary has max weight as key and price list of items picked as value
      solution_list=[] #Empty list to store the solution list. List of lists of prices of items picked
            
      for max_wt in f_list:  #Iterate through each family members weight limit
        if max_wt in opt_dict.keys():
          solution_list.append(opt_dict[max_wt])
        else: #Calculate by calling knapsack function
          solution=knapsack(max_wt,price_weight_list)
          opt_dict[max_wt]=solution #Storing the solution
          solution_list.append(solution)
            
      total_val = 0 #Total value of prices of all items picked by all family members.
      for solution in solution_list: #Calc total value
        total_val+=sum(solution)
            
      price_list={} #Will store the prices of each item
            
      for index,pr_wt_pair in enumerate(price_weight_list):
        if pr_wt_pair[0] in price_list:
          price_list[pr_wt_pair[0]].append(str(index+1))
        else:
          price_list[pr_wt_pair[0]]=[str(index+1)]
            
      outputFile.write("Test Case {}\n".format(test_case+1))
      outputFile.write("Total Price {}\n".format(total_val))
      outputFile.write("Member Items\n")
      for fam in range(f):
        price_dict=price_list.copy()
        price_sol=solution_list[fam]
        index_list=[]
        for price in price_sol:
          index_list.append(price_dict[price][0])
          price_dict[price]=price_dict[price][1:]

        outputFile.write("{}: {}\n".format(fam+1," ".join(index_list)))
        outputFile.write("\n".format(fam+1," ".join(index_list)))

  outputFile.close()

if __name__ == "__main__":
    main()
