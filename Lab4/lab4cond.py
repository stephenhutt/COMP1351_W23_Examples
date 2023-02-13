#Get input and convert to float - will error if a float is not givenß
num = int(input("How many red balloons would you like: "))

#If number is strictly less than 99
if num < 99:
    print("I have more balloons than that")
else:
    print("I don't have that many balloons")