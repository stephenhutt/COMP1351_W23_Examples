
#is a number divisible by 2 and 3?

number = 9

#Is number divisible by 2
if number % 2 ==0:
    #Is number divisible by 3
    if number %3 == 0:
        print (f"{number} is divisible by 2 and 3")
    else:
        print("In Else")