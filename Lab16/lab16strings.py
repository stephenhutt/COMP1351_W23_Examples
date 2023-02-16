"""
Author: Stephen Hutt
Course: 1351
Content: In Class Demo
"""
myStringList = ["Ryan", "Stephen", "Boris", "James"]

#Content Based Loop
for name in myStringList:
    print(len(name))

myString = "Hello World"
print(len(myString))
#Index based loop
for i in range(len(myString)):
    #Print 1 character
    print(myString[i])

print(myString.index("l"))