#Everything is the same here as question one, with the exception of filtering out duplicate book entries for an author
class Author:
    def __init__(self,name):
        self.name = name
        self.books = []

    def publish(self,title):
        #If the book is not found within the list, it will be appended to the list. If the list already contains it, the else statement is run and prompts the user
        if title not in self.books:
            self.books.append(title)
        else:
            print('There were multiple attempts to publish the book','"' + ", ".join(self.books) + '"', 'by',self.name + '. Only one instance will be added to the list for this author.')

    def __str__(self):
        titles = ', '.join(self.books) or 'Author currently has no published books'
        return f'{self.name}. Books: {titles}'

def main():
    darrenShan = Author('Darren Shan')
    darrenShan.publish('A Living Nightmare')
    darrenShan.publish('A Living Nightmare')
    print('Author:', darrenShan)

    hiromuArakawa = Author('Hiromu Arakawa')
    hiromuArakawa.publish('The Land of Sand')
    hiromuArakawa.publish('An Abducted Alchemist')
    hiromuArakawa.publish('The Valley of White Petals')
    print('Author:', hiromuArakawa)

    example = Author('Example Author')
    print('Author:', example)

main()