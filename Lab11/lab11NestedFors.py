"""
Author: Stephen Hutt
Course: 1351
Content: In Class Demo
"""

#Print Double new line
print("\n")


for i in range(1,5):
    print (f"Loop 1_{i}", end="|")
    for j in range(1,i):
        # Print each loop iteration number on the same line
        print(f"{i} * {j} = {i*j}", end= " ~ ")
    #Create a new line
    print("")
