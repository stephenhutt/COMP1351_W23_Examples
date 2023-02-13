"""
Author: Stephen Hutt
Course: 1351
Content: In Class Demo
"""

import dudraw

card_values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
card_suits = ["Spades", "Hearts", "Diamonds", "Clubs"]



#Content based List Iteration
for value in card_values:
    print(value)

#Index based Iteration
for i in range(len(card_values)):
    print(card_values[i])

