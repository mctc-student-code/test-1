#Import used to check special characters
import re

#list of special characters
regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')


def convertSentence(userInput):
    if(len(userInput) == 0): 
        print("You forgot to type in a sentence.")
        main()
    elif(userInput[0].isdigit()):
        print("Numbers cannot be used at the beginning of a variable name.")
        main()
    #Checks for special characters / Validation
    elif(regex.search(userInput) == None):
        convertedString = '' 
        convertedString += userInput[0].lower()
        for i in range(1, len(userInput)): 
            if (userInput[i] == ' '): 
                convertedString += userInput[i + 1].upper() 
                i += 1
            elif(userInput[i - 1] != ' '): 
                convertedString += userInput[i]  
        print(convertedString)
    else:
        print("Special characters are invalid when creating a variable name.")
        main()

#Grabs and passes userInput to "convertSentence"                
def main(): 
    userInput = input("Please enter in a sentence: ")
    convertSentence(userInput.lower())

main()