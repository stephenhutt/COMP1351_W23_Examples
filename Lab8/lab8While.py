"""
Author: Stephen Hutt
Course: 1351
Content: In Class Demo
"""

x = False
score = 0
import random
#this will run forever if you change x
while x:
    print("Eternal")

yourNumber = input("Please enter a something: ")
print(yourNumber.isalpha())


while score < 3:
    myNumber = random.random() * 10
    yourNumber = int(input("Please enter a number: "))
    if yourNumber < myNumber:
        print("You win", end="~")
        
        score += 1
        print(f"Your Score {score}", end="~")
    else:
        print("You lose",end="~")
        print(f"Your Score {score}", end="~")

    