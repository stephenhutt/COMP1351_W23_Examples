myDictionary = {
    "a" : "hello",
    "b" : 456,
    "c" : True
}


print(myDictionary["b"])# prints 456
print(myDictionary["c"])# prints True

myDictionary["a"] ="goodbye"
# replace "hello" with "goodbye"

#Get User Input
newKey = input("Please Enter a Key")
#Standardize the user input
newKey = newKey.lower().strip()
#Print only if the key is in the dictionary
if newKey in myDictionary:
    print(myDictionary[newKey])
else:
    print("Not a valid key")