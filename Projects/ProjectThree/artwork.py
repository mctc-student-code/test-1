import sqlite3
import os

#Create database
db = os.path.join('database', 'artwork.db')

conn = sqlite3.connect(db)

class Artwork:
    def __init__(self, title, artist, email, price, availability = False, id = None):
        self.title = title 
        self.artist = artist
        self.email = email
        self.price = price
        self.availability = availability 
        self.id = id

        self.database = Database()

    #Adds new artist or updates artwork for pre-existing artist if possible
    def save_new_artist(self):
            self.database._add_artist(self)

class Database:

    instance = None

    class __Database:

        def __init__(self):

            # artist_id used to link tables
            artist_table = 'CREATE TABLE IF NOT EXISTS artiststable (artist_id INTEGER PRIMARY KEY, artist TEXT, email TEXT UNIQUE, UNIQUE(email COLLATE NOCASE))'
            artwork_table = 'CREATE TABLE IF NOT EXISTS artworktable (artist_id INTEGER, artwork_id INTEGER PRIMARY KEY, title TEXT, price REAL, availability BOOLEAN, FOREIGN KEY(artist_id) REFERENCES artiststable(artist_id))'

            conn = sqlite3.connect(db)
        
            with conn:
                conn.execute(artist_table)
                conn.execute(artwork_table)

            conn.close()

        #If artist not found by name/email, the new artist is added.
        def _add_artist(self,artwork):
            
            add_artist = 'INSERT INTO artiststable (artist, email) VALUES (?, ?)'
            add_artwork = 'INSERT INTO artworktable (artist_id, title, price, availability) VALUES (?, ?, ?, ?)'

            try: 
                with sqlite3.connect(db) as conn:
                    conn.execute(add_artist, (artwork.artist, artwork.email))
            except Exception:
                print("\nArtist already exists, or invalid combination of artist name and email was blocked. Attemping to check for an existing artist, if found a new piece of artwork will be added.\n")
            finally:
                conn.close()

            #Pre-existing artist found or the user tried using duplicate information, if artist found it will instead just add a new piece of artwork for them.
            try: 
                with sqlite3.connect(db) as conn:
                    existant_id  = conn.execute("SELECT artist_id FROM artiststable WHERE email = ? AND artist = ?",(artwork.email,artwork.artist))
                    exist_id = existant_id.fetchone()
                    artist_id = exist_id[0]

                    duplicate_title_check = conn.execute("SELECT artist_id, title FROM artworktable WHERE artist_id = ? AND title = ?",(artist_id,artwork.title))

                    result = duplicate_title_check.fetchone() #Returns boolean value to check for pre-existing entry

                    if result:
                        print("Artwork already found with this title. Returning back to main menu.\n")
                    else:
                        add_new_artwork = conn.execute(add_artwork, (artist_id,artwork.title, artwork.price, artwork.availability))
                        artwork.id = add_new_artwork.lastrowid
            except Exception:
                print("\nInvalid combination of artist name and email, returning to main menu.\n")
            finally:
                conn.close()
        
        #Grabs all artwork by artist using their unique email and artist_id as a PK for secondary table
        def get_all_by_artist(self,term):
            try: 
                with sqlite3.connect(db) as conn:
                    print("\n")
                    existant_id  = conn.execute("SELECT artist_id FROM artiststable WHERE email = ?", [term])
                    exist_id = existant_id.fetchone()
                    artist_id = exist_id[0]

                    rows = conn.execute('SELECT title, price, availability FROM artworktable WHERE artist_id = ?', [artist_id])

                    results = rows.fetchall() #Returns boolean value to check for pre-existing entry

                    if not results:
                        print("No results found with this artist's name and email combination.")
                    
                    for x in results:
                        availability_translated = ""
                        if x[2] == 0:
                            availability_translated = "Available"
                        else:
                            availability_translated = "Sold"
                        print("Title: ",(x[0]), " Price: $" + str(x[1]), " Availability: ", availability_translated)
                    print("\n")
            except Exception:
                print("\nNo such artist found with this email.\n")

        #Checks for available artwork using "availbility" boolean
        def get_available_by_artist(self,term):
            try: 
                with sqlite3.connect(db) as conn:
                    existant_id  = conn.execute("SELECT artist_id FROM artiststable WHERE email = ?", [term])
                    exist_id = existant_id.fetchone()
                    artist_id = exist_id[0]

                    rows = conn.execute('SELECT title, price FROM artworktable WHERE artist_id = ? AND availability = 0', [artist_id])

                    results = rows.fetchall() #Returns boolean value to check for pre-existing entry
                    
                    for x in results:
                        print("Title: ",(x[0]), " Price: $" + str(x[1]))
                    print("\n")
            except Exception:
                print("\nNo such artist found with this email.\n")

        #Changes availability for artwork by artist based on PK found in "artworktable"
        def change_availability(self,search_criteria):
            title = search_criteria[0]
            email = search_criteria[1]

            try: 
                with sqlite3.connect(db) as conn:
                    existant_id  = conn.execute("SELECT artist_id FROM artiststable WHERE email = ?", [email])
                    exist_id = existant_id.fetchone()
                    artist_id = exist_id[0]

                    rows = conn.execute('SELECT availability FROM artworktable WHERE artist_id = ? AND title = ?', (artist_id,title))

                    results = rows.fetchone() #Returns boolean value to check for pre-existing entry

                    if results:
                        availability = results[0]
                        if availability == 0:
                            conn.execute('UPDATE artworktable SET availability = ? WHERE title = ?', (1,title))
                        else:
                            conn.execute('UPDATE artworktable SET availability = ? WHERE title = ?', (0,title))
                    else:
                        print("\nNo artwork was found with this title using the following email.\n")
            except Exception:
                print("\nError - email doesn't exist in the database.\n")

        #Deletes row (artwork) based on PK/email
        def delete_artwork(self,search_criteria):
            title = search_criteria[0]
            email = search_criteria[1]

            try: 
                with sqlite3.connect(db) as conn:
                    existant_id  = conn.execute("SELECT artist_id FROM artiststable WHERE email = ?", [email])
                    exist_id = existant_id.fetchone()
                    artist_id = exist_id[0]

                    rows = conn.execute('SELECT * FROM artworktable WHERE artist_id = ? AND title = ?', (artist_id,title))

                    results = rows.fetchone()

                    if results:
                        conn.execute('DELETE FROM artworktable WHERE artist_id = ? AND title = ?',(artist_id,title))
                    else:
                        print("\nNo artwork was found with this title using the following email.\n")
            except Exception:
                print("\nError - email doesn't exist in the database.\n")

    def __new__(cls):
        if not Database.instance:
            Database.instance = Database.__Database()
        return Database.instance


    def __getattr__(self, name):
        return getattr(self.instance, name)


    def __setattr__(self, name, value):
        return setattr(self.instance, name, value)

class ArtistError(Exception):
    pass