from artwork import Artwork, Database
import validation

run_program = True
menu_options = True

database = Database()

def add_artwork():
    try:
        add_artwork = validation.get_new_artist_info()
        add_artwork.save_new_artist()
    except Exception as e:
        print(e)

def search_all_by_artist():
    email = validation.get_artist_by_email()
    found = database.get_all_by_artist(email)

def search_available_by_artist():
    email = validation.get_artist_by_email()
    found = database.get_available_by_artist(email)

def change_availability_by_artist():
    search_criteria = validation.get_artwork_by_title_and_email()
    found = database.change_availability(search_criteria)

def delete_artwork_by_artist():
    search_criteria = validation.get_artwork_by_title_and_email()
    found = database.delete_artwork(search_criteria)    

def main():
    global run_program
    global menu_options
    
    while run_program == True:
        while menu_options == True:
            print("-----------TEST-----------")
            print("1: Add New Artist/Artwork") #Adds artist is not pre-existing, if artist exists it tries to add a new piece of artwork for that artist with PK
            print("2: Search All Artwork By Artist")
            print("3: Search Available Artwork By Artist")
            print("4: Change Availability Status Of An Artwork")
            print("5: Delete an artwork")
            print("6: Quit\n")
            choice = input("Please type select an option from the menu: ")
            print('\n')
            
            if choice == "1":
                add_artwork()
            elif choice == "2":
                search_all_by_artist()
            elif choice == "3":
                search_available_by_artist()
            elif choice == "4":
                change_availability_by_artist()
            elif choice == "5":
                delete_artwork_by_artist()
            elif choice == "6":
                run_program = False
                menu_options = False
            else:
                print("\n Not Valid Choice Try again")
                break

if __name__ == '__main__':
    main()