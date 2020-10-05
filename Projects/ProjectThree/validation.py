from artwork import Artwork
import re

#Used when checking for email format
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

#Parameters are used for tests in this case, not necessarily needed for the program itself to function.

def valid_title(title):
    while True:
        title = input('Enter artwork title: ').strip().title()
            
        if not title.replace(' ','').isalpha():
            print("Input was either empty or contained an invalid character, please try again.")
            continue
        else:
            title = re.sub(' +', ' ', title)
            break

    return title

def valid_artist(*argv):
    while True:
        first_name = input('Enter artist\'s First name: ').strip().title()
        if not first_name.isalpha():
            print("Please enter a valid first name only including letters.")
            continue
        else:
            break

    while True:
        last_name = input('Enter artist\'s Last name: ').strip().title()
        if not last_name.isalpha():
            print("Please enter a valid last name only including letters.")
            continue
        else:
            break
        
    artist = first_name + " " + last_name
    return artist

def valid_email(email):
    while True:
        email = input('Enter artist\'s email: ').strip()
        if not (re.search(regex,email)):
            print("Please enter a valid email address using all undercase letters.")
            continue
        else:
            break

    return email

def valid_price(price):
    while True:
        price = input("Please enter price of artwork in dollars: ")
        try:    
            price = float(price)
            if price > 0:
                break
            else:
                print("Please type in a number greater than 0.")
                continue
            break
        except ValueError:    
            print("Please enter in a valid price.")
            continue

    return price

def get_new_artist_info():
    title = ""
    artist = ""
    email = ""
    price = 0

    title = valid_title(title)
    artist = valid_artist(artist)
    email = valid_email(email)
    price = valid_price(price)

    return Artwork(title,artist,email,price) #Create object with following attributes

def get_artist_by_email():
    email = ""
    
    email = valid_email(email)
    return email

def get_artwork_by_title_and_email():
    title = ""
    email = ""
    
    title = valid_title(title)
    email = valid_email(email)
    return title,email