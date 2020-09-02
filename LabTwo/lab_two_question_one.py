class Author:
    def __init__(self,name):
        self.name = name
        self.books = []

    def publish(self,title):
        self.books.append(title)

    def __str__(self):
        #Attempts to join the strings (books) with comma's to print later, if the list returns empty it prints the statement after the "or" condition
        titles = ', '.join(self.books) or 'Author currently has no published books'
        return f'{self.name}. Books: {titles}'

def main():
    #Passes name to string to the name object
    darrenShan = Author('Darren Shan')
    #Passes the book name to the publish method where its added to a list
    darrenShan.publish('A Living Nightmare')
    darrenShan.publish('The Vampire\'s Assistant')
    print("Author:", darrenShan)

    hiromuArakawa = Author('Hiromu Arakawa')
    hiromuArakawa.publish('The Land of Sand')
    hiromuArakawa.publish('An Abducted Alchemist')
    hiromuArakawa.publish('The Valley of White Petals')
    print("Author:", hiromuArakawa)

    #Test to show what happens if an author being added has no currently books published
    example = Author("Example Author")
    print("Author:", example)

main()