myList = [5,6,7,8]

target = 5


if myList.count(target) > 0:
    # !
    print(f"{target} is in my list")

if target in myList:
    print(f"{target} is in my list")

if "s" in "Apples":
    print("Apples contains \"s\"")
myStr = "~".join(["      A", "B", "C"])
print (myStr)
#Which of these is easier to read

myStr = myStr.strip()
print(myStr.count(","))
print(myStr.find(","))
print(myStr.split("~"))