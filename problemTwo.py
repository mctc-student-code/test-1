lst = []

#Ask user for number of classes
numOfClasses = int(input("How many classes are you taking this semester? "))

#Itterations based on number of classes, appends each user response to the list
for i in range(0,numOfClasses):
    className = str(input("Please enter class name: "))
    lst.append(className)

#Print out each item within the list, one per line
for i in range(0,len(lst)):
    print("Registered for: ",lst[i])