

myList = ["Beatrice", "Benedict", "Claudio", "Hero"]

print(myList[2:])

# print(myList.index("Romeo"))

def containsSec(myList,num):
    if myList.count(num) > 0:
        return True
    else:
        return False

def contains(myList, num):
    for i in range(len(myList)):
        if myList[i] == num:
            return True
    return False

print(containsSec(myList[3:], "Claudio"))
print(containsSec(myList, "Romeo"))