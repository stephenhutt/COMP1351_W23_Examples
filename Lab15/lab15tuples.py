"""
Author: Stephen Hutt
Course: 1351
Content: In Class Demo
"""

myList = ["Beatrice", "Benedict", "Claudio", "Hero"]
myTuple = ("Winter", "Spring", "Summer", "Fall")

print(len(myTuple))
print(myTuple.index("Summer"))
print(myTuple.count("Summer"))

exit()
mySecondList = []
for i in range(len(myList)):
    print(myList[i])
    mySecondList.append((myTuple[i], myList[i]))

print(mySecondList)

print(len(mySecondList))
print(len(mySecondList[0]))