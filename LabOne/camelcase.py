#Import used to check special characters
import re

#list of special characters
regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

def convertSentence(userInput):
    userInput = userInput.strip()
    
    if(len(userInput) == 0 or userInput == " "): 
        print("You forgot to type in a sentence.")
        main()
    elif(userInput[0].isdigit()):
        print("Numbers cannot be used at the beginning of a variable name.")
        main()
    #Checks for special characters / Validation
    elif(regex.search(userInput) == None):
        userInput = ''.join(x for x in userInput.title() if x.isalnum())
        userInput = userInput[0].lower() + userInput[1:]
        print(userInput)
        return userInput
    else:
        print("Special characters are not allowed. Please type in a new sentence.")
        main()

def display_banner():
	""" Display program name in banner """
	msg = 'AWSOME camelCaseGenerator PROGRAM'
	stars = '*' * len(msg)
	print(f'\n {stars} \n {msg} \n {stars}\n')

def display_instructions():
    print('Enter a sentence to convert to camelCase') 

#Grabs and passes userInput to "convertSentence"                
def main():
    display_banner()
    display_instructions()
    userInput = input()
    convertSentence(userInput.lower())


if __name__ == '__main__':
    main()