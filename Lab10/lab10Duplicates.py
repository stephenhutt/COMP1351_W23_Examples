"""
Author: Stephen Hutt
Course: 1351
Content: In Class Demo
"""

def findDuplicates(a, b, c):
    """test if there are any duplicates in three parameters
    param: float a: variable to check
    param: float b: variable to check
    param: float c: variable to check
    return: bool"""
    if a==b:
        return True
    elif b==c:
        return True 
    elif c==a:
        return True 
    else:
        return False
    return False 

if findDuplicates(10,10,5):
    print("Duplicates")

