import sqlite3

#Create database
conn = sqlite3.connect('record.db')

#Create a cursor
cursor = conn.cursor()

#Global variables
run_program = True
menu_options = True

#Create a table
cursor.execute("""CREATE TABLE IF NOT EXISTS records (
        name TEXT,
        country TEXT,
        catches INTEGER
    )""")

def add_record():
    add_first_name = ""
    add_second_name = ""
    add_country = ""
    add_catches = 0

    while True:
        name = input('Enter a first name using only alphanumeric characters: ')
        if name.isalpha():
            add_first_name = name.lower()
            break

    while True:
        name = input('Enter a second name using only alphanumeric characters: ')
        if name.isalpha():
            add_second_name = name.lower()
            break
    
    while True:
        country = input("Please enter in a 2-3 letter country abbreviation: ")
        if country.isalnum():
            if len(country) > 1 and len(country) < 4:
                add_country = country.upper()
                break

    while True:
        catches = input("Please input number of catches: ")
        if catches.isdigit():
            if int(catches) > 0:
                add_catches = catches
                break

    add_name = add_first_name + " " + add_second_name

    cursor.execute("""INSERT INTO records(name, country, catches) 
    VALUES (?,?,?)""", (add_name, add_country, add_catches))
    conn.commit
    print('\n')

    main()

def search_record():
    search_first_name = ""
    search_second_name = ""

    while True:
        name = input('Enter a first name using only alphanumeric characters: ')
        if name.isalpha():
            search_first_name = name.lower()
            break

    while True:
        name = input('Enter a second name using only alphanumeric characters: ')
        if name.isalpha():
            search_second_name = name.lower()
            break

    search_name = search_first_name + " " + search_second_name

    results = cursor.execute("SELECT * FROM records WHERE name = (?)", search_name)
    print_results = results.fetchall()

    for item in print_results:
        print(item)

    main()

def update_record():
    update_first_name = ""
    update_second_name = ""
    add_catches = 0

    while True:
        name = input('Enter a first name using only alphanumeric characters: ')
        if name.isalpha():
            update_first_name = name.lower()
            break

    while True:
        name = input('Enter a second name using only alphanumeric characters: ')
        if name.isalpha():
            update_second_name = name.lower()
            break

    while True:
        catches = input("Please input number of catches: ")
        if catches.isdigit():
            if int(catches) > 0:
                add_catches = catches
                break

    update_name = update_first_name + " " + update_second_name
    string_catches = str(add_catches)

    cursor.execute("UPDATE records SET catches = (?) WHERE name = (?", string_catches, update_name)
    conn.commit
    print('\n')

    main()

def delete_record():
    remove_first_name = ""
    remove_second_name = ""

    while True:
        name = input('Enter a first name using only alphanumeric characters: ')
        if name.isalpha():
            remove_first_name = name.lower()
            break

    while True:
        name = input('Enter a second name using only alphanumeric characters: ')
        if name.isalpha():
            remove_second_name = name.lower()
            break

    remove_name = remove_first_name + " " + remove_second_name

    cursor.execute("DELETE from records WHERE name = (?)", remove_name)
    conn.commit
    print('\n')
    
    main()

def main():
    global run_program
    global menu_options
    
    while run_program == True:
        while menu_options == True:
            print("Chainsaw Juggling Record Holders as of July 2018\n")
            print("-----Options-----")
            print("1: Add record")
            print("2: Search record")
            print("3: Update record")
            print("4: Delete record")
            print("5: Quit\n")
            choice = input("Please type select an option from the menu: ")
            
            if choice == "1":
                add_record()
            elif choice == "2":
                search_record()
            elif choice == "3":
                update_record()
            elif choice == "4":
                delete_record()
            elif choice == "5":
                run_program = False
                menu_options = False
                return run_program, menu_options
            else:
                print("\n Not Valid Choice Try again")
                break

main()

#Commit our command
conn.commit()

#Close our connection
conn.close()