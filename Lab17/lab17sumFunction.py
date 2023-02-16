def find_sum(the_list:list[int]) ->int:
    #Create a variable for our total so far 
    total = 0
    for num in the_list: #loop through all the numbers in our list
        total += num # add the number to the total
    #once the loop is complete, total will be the sum of all numbers in the list    
    return total # return our sum value


def find_average(the_list:list[int]) ->float:
    total = 0

    for num in the_list:
        total += num

    return total/ len(the_list)




some_numbers = [34,511,467,21,7,24]
print(find_sum(some_numbers))