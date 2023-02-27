# Question 3
for i in range(3):
    for j in range(7):
        #print("OX", end="")
        if j % 2 == 0:
            print("O", end="")
        else:
            print("X", end="")
    print()

# Question 4
sentence = "The Quick brown fox jumps over the lazy dog"

#Print T
print(sentence[0])
#Print quick - not lower case q
quickVar = sentence[4:9]
quickVar = quickVar.lower()

print(quickVar)

#Print backwards 
print(sentence[-1:-9:-1])



#Question 1
numbers = [1.23, 2.14, 5.34, 3.01]
for num in numbers:
    if num > 2:
        print(num)

#Question 7
password = input("Enter Password: ")
password = password.lower()
while not password == "open sesame":
    print("Nope")
    password = input("Enter Password: ")
    password = password.lower()
    print(password)
print("Congrats")