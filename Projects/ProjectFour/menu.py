run_program = True
menu_options = True

def function_one():
    print("Placeholder")

def function_two():
    print("Placeholder")

def function_three():
    print("Placeholder")

def function_four():
    print("Placeholder")

def function_five():
    print("Placeholder")  

def main():
    global run_program
    global menu_options
    
    while run_program == True:
        while menu_options == True:
            print("-----------Menu Options-----------")
            print("1:") #Adds artist is not pre-existing, if artist exists it tries to add a new piece of artwork for that artist with PK
            print("2:")
            print("3:")
            print("4:")
            print("5:")
            print("6:")
            choice = input("Please type select an option from the menu: ")
            print('\n')
            
            if choice == "1":
                function_one()
            elif choice == "2":
                function_two()
            elif choice == "3":
                function_three()
            elif choice == "4":
                function_four()
            elif choice == "5":
                function_five()
            elif choice == "6":
                run_program = False
                menu_options = False
            else:
                print("\n Not Valid Choice Try again")
                break

if __name__ == '__main__':
    main()