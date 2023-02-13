"""
Author: Stephen Hutt
Course: 1351
Content: In Class Demo
"""

def findfactorial(num):
    """Calculate the factorial of a number
    param: int num: variable to check
    return: int"""
    result = num 
    num = num -1
    while num > 0:
        result = result * num
        num = num - 1
    return result

def triangleNumber(num):
    #Initialise our return variable as 0
    result = 0
    #for loop
    for i in range(1,num+1):
        #add the iteration number to the result
        result = result + i
    # return the result
    return result 

print(findfactorial(2) + findfactorial(5))
print(triangleNumber(2))        