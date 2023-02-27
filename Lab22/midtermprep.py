



for i in range(3):
    for j in range(7):
        #print("OX", end="")
        if j % 2 == 0:
            print("O", end="")
        else:
            print("X", end="")
    print()


sentence = "The Quick brown fox jumps over the lazy dog"

print(sentence[0])

quickVar = sentence[4:9]
quickVar = quickVar.lower()

print(quickVar)

print(sentence[-1:-9:-1])



numbers = [1.23, 2.14, 5.34, 3.01]
for num in numbers:
    if num > 2:
        print(num)


password = input("Enter Password: ")
while not password.lower() == "open sesame":
    print("Nope")
    password = input("Enter Password: ")
print("Congrats")