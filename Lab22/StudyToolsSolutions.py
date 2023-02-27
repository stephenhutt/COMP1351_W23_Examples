import random
#Question 1
def everyOther(myList):
    for i in range(len(myList)):
        if i % 2 == 0:
            print (myList[i])

#Question 2
def product(myList):
    answer = 1
    for num in myList:
        answer = answer * num
    return answer

#Question 3
def firstFive(myStr):
    if len(myStr) < 5:
        return myStr.upper()
    else:
        return myStr[:5].upper()
    
#Question 4
def xbyx(x):
    for i in range(x):
        for j in range(x):
            num = int(random.random() * 10)
            print(num, end="~")
            
        print()


xbyx(5)



myList = [5, 2, 9,12]
for num in myList:
    if num < 10:
        print(num)
        if num%2==0:
            print(num**2)
