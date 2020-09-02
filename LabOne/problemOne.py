#Ask user for name and birth month
name = input("What is your name? ")
month = input("What month were you born in? ")

#Greets the user, specifies the number of letter in their name, if
print("Nice to meet you " + name + "!")
print("Your name contains " + str(len(name)) + " letters.")

if month.lower() == "august":
    print("Happy birthday!")