"""
Author: Stephen Hutt
Course: 1351
Content: In Class Demo
"""
user_number = int(input("Pick A Number:"))

if(user_number % 2 ==1):
    user_number +=2
else:
    user_number -=1
print("your new number is ", user_number)